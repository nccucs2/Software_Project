from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class student_info(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    major=models.TextField(blank=True)
    name=models.TextField(blank=True)
    number=models.CharField(max_length=10)


class course(models.Model):
    AcademicYear = models.IntegerField()
    Semester  = models.IntegerField(null=True)
    course_name = models.TextField()
    credit = models.CharField(max_length=5,blank=True)
    teacher = models.TextField()
#    object = models.CharField(max_length=3,blank=True)
    course_code = models.CharField(max_length=50,primary_key=True)
    course_category = models.CharField(max_length=5,blank=True)
    deparment=models.TextField(blank=True)
    course_type=models.CharField(max_length=5,blank=True)
    general_type=models.CharField(max_length=5,blank=True)
    def __str__(self):
        return str(self.teacher) + " " + str(self.course_name)

class course_grade(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    grade=models.SmallIntegerField()
    grade_range=models.SmallIntegerField(default=0)
    def __str__(self):
        return str(self.user) +  " " + str(self.course)

class gpa(models.Model):
    grade_range = models.ForeignKey(course_grade,on_delete=models.CASCADE,default='',blank=True)
    gpa_count = models.FloatField()
    def __str__(self):
        return str(self.gpa_count)

class personal_info(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField()
    id_number = models.CharField(max_length=10)
    guardian = models.CharField(max_length=10)
    birth = models.DateField()
    phone_number = models.CharField(max_length=10)
    english_name = models.CharField(max_length=20)
    e_mail = models.CharField(max_length=20,default='')
    def __str__(self):
        return str(self.user)


# a = course.objects.all()
# #a.delete()
# f = open('/Users/byron/Desktop/1062_courses_all_cleaned_22.csv','r',encoding='utf-16', errors='ignore')
list=[]
counter = 0
number = 0
"""
for line in f.readlines():
     if counter ==0:
         counter+=1
         continue;
     else:
         AcademicYear=line.strip().split(',')[1]
         Semester=(line.strip().split(',')[3])

         try:
             print(int(Semester))
             number=int(Semester)
         except:
             number=0
             print(0)
         course_name=line.strip().split(',')[4]

         credit=line.strip().split(',')[7]
         teacher=line.strip().split(',')[6]
         course_code=line.strip().split(',')[2]
         deparment=line.strip().split(',')[12]
         course_type=line.strip().split(',')[13]
         general_type=line.strip().split(',')[15]

         #course.objects.create(AcademicYear=AcademicYear,Semester=number,course_name=course_name,credit=(credit),teacher=teacher,course_code=course_code,deparment=deparment,course_type=course_type,general_type=general_type)
         print(AcademicYear,Semester,course_name,credit,teacher,course_code,deparment,course_type,general_type)
         # print(type( Semester))
         counter+=1
         # if counter==10:
         #     break
"""
