from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import student_info,course,course_grade,gpa
# Register your models here.

admin.site.register(student_info)
admin.site.register(course)
admin.site.register(course_grade)
admin.site.register(gpa)
