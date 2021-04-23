from django.contrib import admin
from College.models import *

# Register your models here.
admin.site.register([College, Principle, Department, Teacher, Subject, Student])


chasgds