from django.contrib import admin
from .models import Faculty, Department, Group, Subject, Teacher, Student

admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
