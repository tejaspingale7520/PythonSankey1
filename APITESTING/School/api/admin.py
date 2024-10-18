from django.contrib import admin
from .models import Teacher,Student

# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','subject','email']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','email','enrolled_date','teacher']