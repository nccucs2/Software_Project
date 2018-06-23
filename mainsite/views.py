from django.shortcuts import render,render_to_response
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainsite.models import student_info,course,course_grade,personal_info
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def login(request):
    #template = get_template('login.html')
    if request.user.is_authenticated:
        return HttpResponseRedirect('/student/')
    try:
        username = request.POST['usr_id']
        password = request.POST['usr_pass']
        user = auth.authenticate(username=username, password=password)

    except:
        user = None
        #user_id = None
        #user_password = None

    if user is not None:
        if user.is_active:
            auth.login(request,user)
            return HttpResponseRedirect('/student/')
    else:
        if request.POST:
            messages.error(request,'帳號或密碼錯誤!!')
        return render(request,'login.html')



        #return render_to_response('login.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/identify/')
        else:
            messages.error(request,'輸入格式有誤!')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

def identify(request):
    q = User.objects.all()
    if request.POST:
        p=student_info.objects.create(user=q[len(q)-1],major=request.POST['major'],name=request.POST['name'],number=request.POST['number'])
        p.save();
        return HttpResponseRedirect('/login/')
    return render(request,'identify.html')

def student(request):
    #print(request)
    if request.user.is_authenticated:
        students=student_info.objects.get(user=request.user)
        return render(request,'student.html',{
        'students':students,
        })

    else:
        return HttpResponseRedirect('/login/')

def course2(request):
    print(request.user)
    if request.user.is_authenticated:
        courses=course_grade.objects.filter(user=request.user)
        return render(request,'course.html',{
        'courses':courses,
        })
    return render(request,'course.html')

def suggest_course(request):
    # make a dictionary for course_code
    courses = course.objects.all()
    data={}
    for i in courses:
        data[i.course_code]=0
    """
    for i in data:
        print(data[i])
        print(i)
    """
    #find the person who is the same major
    me = student_info.objects.get(user=request.user)
    my_major = me.major
    student = student_info.objects.all()
    #same major add 5
    for i in student:
        if i.major[:2]==my_major[:2]:
            k = course_grade.objects.filter(user=i.user)
            for j in k :
                data[j.course.course_code]+=5
    #different major add 2
        else:
            k = course_grade.objects.filter(user=i.user)
            for j in k:
                data[j.course.course_code]+=2
    #initial the point to 0 with user's course
    p = course_grade.objects.filter(user=request.user)
    for i in p:
        data[i.course.course_code]=0
    for i in data:
        if data[i]>=25:
            r=course.objects.get(course_code=i)
            print(r)
    return render(request,'suggest_course.html')

def person_info(request):
    if request.user.is_authenticated:
        my_infos=personal_info.objects.get(user=request.user)
        print(my_infos.address)
        return render(request,'personal_info.html',{
        'my_infos':my_infos,
        })
    return render(request,'personal_info.html')

def course_plan(request):

    department_require={"資科":48,"斯語":54,"社會":24,"教育":28}
    department_group={"資科":15,"斯語":6,"社會":18,"教育":12}
    sport = 0
    service = 0
    english = 0
    chinese = 0
    n_science = 0
    s_science = 0
    human = 0
    total_credit_count = 0

    department=student_info.objects.get(user=request.user)
    mydepart = department.major[:2]

    require_credit_left = department_require[mydepart]
    group_credit_left = department_group[mydepart]
    print(mydepart)
    print(require_credit_left)
    print(group_credit_left)

    """所有修過的課程"""
    p = course_grade.objects.filter(user=request.user)

    for i in p:
        if i.course.deparment[:2]==mydepart:
            if i.course.course_type=='必':
                require_credit_left-=int(i.course.credit)

                print('必修:')
                # print(i)
            elif i.course.course_type=='選':
                group_credit_left-=int(i.course.credit)

                print('選修:')
                # print(i)
            elif i.course.course_type=='群':

                print('群修:' )
                # print(i)
            # print(i)
        elif i.course.course_name[:6]=='服務學習課程':
                service+=1
                print("服務")
        elif i.course.course_name[:2]=='體育':
                sport+=1
                print("體育")
        else:
            if i.course.general_type=='社會通識':
                s_science += int(i.course.credit)

                print('社會:')
                # print(i)
            if i.course.general_type=='自然通識':
                n_science += int(i.course.credit)

                print('自然:')
                # print(i)
            if i.course.general_type=='人文通識':
                human += int(i.course.credit)

                print('人文:')
                # print(i)
            if i.course.general_type=='中文通識':
                chinese += int(i.course.credit)

                print('中文')
            if i.course.general_type=='外文通識':
                english += int(i.course.credit)

                print('外文')
            else:
                print('其他')

        total_credit_count+=int(i.course.credit)
        print(i)

    if n_science<4:
        n_science_credit_left = 4 - n_science
        print("自然還剩",n_science_credit_left)
    elif n_science>9:
        total_credit_count -= n_science - 9

    if s_science<4:
        s_science_credit_left = 4 - s_science
        print("社會還剩",s_science_credit_left)
    elif s_science>9:
        total_credit_count -= s_science - 9

    if human<4:
        human_credit_left = 4 - human
        print("人文還剩",human_credit_left)
    elif human>9:
        total_credit_count -= human - 9

    if service<2:
        service_left = 2 - service
        print("服務還剩",service_left)

    if english<4:
        english_credit_left = 4 - english
        print("英文還剩",english_credit_left)
    elif english>6:
        total_credit_count -= english - 6

    if  chinese<3:
        chinese_credit_left = 6 - chinese
        print("中文還剩",chinese_credit_left)
    elif chinese>6:
        total_credit_count -= chinese - 6

    print("必修剩下多少學分",require_credit_left)
    print("群修剩下多少學分",group_credit_left)
    print("總共已修",total_credit_count)


    return render(request,'course_plan.html',locals())
# Create your views here.
