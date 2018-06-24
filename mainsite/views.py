from django.shortcuts import render,render_to_response
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainsite.models import student_info,course,course_grade,personal_info,gpa
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

def course(request):
    print(request.user)
    if request.user.is_authenticated:
        courses=course_grade.objects.filter(user=request.user)
        courses.gpa_list= [];
        my_infos=personal_info.objects.get(user=request.user)
        student = student_info.objects.get(user=request.user)
        person = course_grade.objects.filter(user=request.user)
        counter_credit = 0
        sum = 0
        i_count = 0;
        for i in person:

            # print(i.grade_range.course_name," ",i.grade_range.grade," ",i.grade_count)
            if i.grade>=90 and i.grade<=100:
                courses.gpa_list.append(4.3)
            elif i.grade>=85 and i.grade<=89:
                courses.gpa_list.append(4)
            elif i.grade>=80 and i.grade<=84:
                courses.gpa_list.append(3.7)
            elif i.grade>=77 and i.grade<=79:
                courses.gpa_list.append(3.3)
            elif i.grade>=73 and i.grade<=76:
                courses.gpa_list.append(3)
            elif i.grade>=70 and i.grade<=72:
                courses.gpa_list.append(2.7)
            elif i.grade>=67 and i.grade<=69:
                courses.gpa_list.append(2.3)
            elif i.grade>=63 and i.grade<=66:
                courses.gpa_list.append(2)
            elif i.grade>=60 and i.grade<=62:
                courses.gpa_list.append(1.7)
            elif i.grade>=50 and i.grade<=59:
                courses.gpa_list.append(1)
            else:
                courses.gpa_list.append(0)


            print(i.course.course_name," ",i.grade," ",i.grade_range)
            sum+=int(i.grade)*int(i.course.credit)
            counter_credit+=int(i.course.credit)

        sum_gpa = 0
        i = 0
        for course in courses:
            course.gpa = courses.gpa_list[i]
            sum_gpa += courses.gpa_list[i]*int(course.course.credit)
            i+=1


        average_grade = round(float(sum/counter_credit),2)
        average_gpa = round(float(sum_gpa/counter_credit),2)
        print(average_grade)
        print(average_gpa)
        print(counter_credit)
    return render(request,'course.html',locals())

def suggest_course(request):
    return render(request,'suggest_course.html')

def person_info(request):
    if request.user.is_authenticated:
        my_infos=personal_info.objects.get(user=request.user)
        student = student_info.objects.get(user=request.user)
        print(my_infos.address)
        # return render(request,'personal_info.html',{
        # 'my_infos':my_infos,
        # })
        return render(request,'personal_info.html',locals())
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

    # student = student_info.objects.get(user=request.user)
    department=student_info.objects.get(user=request.user)
    mydepart = department.major[:2]

    require_credit_left = department_require[mydepart]
    require_credit = department_require[mydepart]
    group_credit_left = department_group[mydepart]
    group_credit = department_group[mydepart]
    print(mydepart)
    print(require_credit_left)
    print(group_credit_left)
    require = 0
    select = 0
    group = 0
    other = 0
    """所有修過的課程"""
    p = course_grade.objects.filter(user=request.user)

    for i in p:
        if i.course.deparment[:2]==mydepart:
            if i.course.course_type=='必':
                require_credit_left-=int(i.course.credit)
                require += int(i.course.credit)
                print('必修:')
                # print(i)
            elif i.course.course_type=='選':
                # group_credit_left-=int(i.course.credit)
                select+=int(i.course.credit)
                print('選修:')
                # print(i)
            elif i.course.course_type=='群':
                group_credit_left-=int(i.course.credit)
                group+=int(i.course.credit)
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
            elif i.course.general_type=='自然通識':
                n_science += int(i.course.credit)

                print('自然:')
                # print(i)
            elif i.course.general_type=='人文通識':
                human += int(i.course.credit)

                print('人文:')
                # print(i)
            elif i.course.general_type=='中文通識':
                chinese += int(i.course.credit)

                print('中文:')
            elif i.course.general_type=='外文通識':
                english += int(i.course.credit)

                print('外文:')
            else:
                other += int(i.course.credit)
                print('其他:')

        total_credit_count+=int(i.course.credit)
        print(i)


    if n_science<4:
        n_science_credit_left = 4 - n_science
        print("自然還剩",n_science_credit_left)
    else:
        if n_science>9:
            total_credit_count -= n_science - 9
        n_science_credit_left = 0

    if s_science<4:
        s_science_credit_left = 4 - s_science
        print("社會還剩",s_science_credit_left)
    else:
        if s_science>9:
            total_credit_count -= s_science - 9
        s_science_credit_left = 0

    if human<3:
        human_credit_left = 4 - human
        print("人文還剩",human_credit_left)
    else:
        if human>9:
            total_credit_count -= human - 9
        human_credit_left = 0
    if sport<4:
        sport_left = 4-sport
        print("體育還剩",sport_left)
    else:
        sport_left = 0
    if service<2:
        service_left = 2 - service
        print("服務還剩",service_left)
    else:
        service_left = 0

    if english<4:
        english_credit_left = 4 - english
        print("英文還剩",english_credit_left)
    else:
        if english>6:
            total_credit_count -= english - 6
        english_credit_left = 0

    if  chinese<3:
        chinese_credit_left = 6 - chinese
        print("中文還剩",chinese_credit_left)
    else:
        if chinese>6:
            total_credit_count -= chinese - 6
        chinese_credit_left = 0

    science_require = "4~9"
    social_require = "3~9"
    human_require = "3~9"
    service_require = 2
    sport_require = 4
    english_require = "4~6"
    chinese_require = "3~6"
    language_require ="7~12"
    gerneral_require = "28~32"

    language_total_left = english_credit_left+chinese_credit_left
    general_total_left = n_science_credit_left + s_science_credit_left+human_credit_left
    print("必修剩下多少學分",require_credit_left)
    print("群修剩下多少學分",group_credit_left)
    print("必修",require)
    print("選修",select)
    print("群修",group)
    print("其他",other)
    print("中文",chinese)
    print("外文",english)
    print("自然",n_science)
    print("社會",s_science)
    print("人文",human)
    print("總共已修",total_credit_count)


    return render(request,'course_plan.html',locals())
# Create your views here.
