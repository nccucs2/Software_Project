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


class course_grade(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    grade=models.SmallIntegerField()
    grade_range=models.SmallIntegerField(default=0)


class gpa(models.Model):
    grade_range = models.ForeignKey(course_grade,on_delete=models.CASCADE)
    gpa_count = models.FloatField()
