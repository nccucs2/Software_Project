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
    Semester  = models.IntegerField()
    course_name = models.TextField()
    credit = models.DecimalField(max_digits=2,decimal_places=1)
    teacher = models.TextField()
    course_code = models.CharField(max_length=50,primary_key=True)
    course_category = models.CharField(max_length=5,blank=True)
    department = models.TextField(blank=True)
    course_type = models.CharField(max_length=5,blank=True)
    general_type = models.CharField(max_length=5,blank=True)
    def __str__(self):
        return self.teacher + " " + self.course_name

class course_grade(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    grade=models.SmallIntegerField()
    grade_range=models.SmallIntegerField(default=0)
    def __str__(self):
        return self.user +  " " + self.course

class gpa(models.Model):
    grade_range = models.ForeignKey(course_grade,on_delete=models.CASCADE)
    gpa_count = models.FloatField()
    def __str__(self):
        return self.gpa_count

class personal_info(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField()
    id_number = models.CharField(max_length=10)
    guardian = models.CharField(max_length=10)
    birth = models.DateField()
    phone_number = models.IntegerField()
    english_name = models.CharField(max_length=20)
    def __str__(self):
        return self.user
