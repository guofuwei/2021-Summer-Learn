from django.contrib import admin
from .models import StudentInfo,InterviewInfo,student_admin
# Register your models here.
admin.site.register(StudentInfo,student_admin)
admin.site.register(InterviewInfo)