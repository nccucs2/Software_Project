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

def course(request):
    print(request.user)
    if request.user.is_authenticated:
        courses=course_grade.objects.filter(user=request.user)
        return render(request,'course.html',{
        'courses':courses,
        })
    return render(request,'course.html')

def suggest_course(request):
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
    department=student_info.objects.get(user=request.user)
    mydepart = department.major[:2]
    print(mydepart)
    p = course_grade.objects.filter(user=request.user)
    for i in p:
        if i.course.deparment[:2]==mydepart:
            if i.course.course_type=='必':
                print('必修:')
                print(i)
            elif i.course.course_type=='選':
                print('選修:')
                print(i)
            elif i.course.course_type=='群':
                print('群修' )
                print(i)
    for i in p :
        if i.course.general_type=='社會通識':
            print('社會')
            print(i)
        if i.course.general_type=='自然通識':
            print('自然')
            print(i)
        if i.course.general_type=='人文通識':
            print('人文')
            print(i)

    return render(request,'course_plan.html')
# Create your views here.
