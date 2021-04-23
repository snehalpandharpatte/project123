from django.contrib import admin
from aadhar.models import Person, Adhar

# Register your models here.

admin.site.register([Person, Adhar])