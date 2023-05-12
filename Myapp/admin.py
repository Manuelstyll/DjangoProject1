from django.contrib import admin
from Myapp.models import Student
from Myapp.models import assignment
from Myapp.models import newitem
from Myapp.models import olditem

# Register your models here.
admin.site.register(Student)
admin.site.register(assignment)
admin.site.register(newitem)
admin.site.register(olditem)