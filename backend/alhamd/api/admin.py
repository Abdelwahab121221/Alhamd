from django.contrib import admin
from .models import Teacher , Student , Assistants
'''
username > admin
password > Alhamd160@
'''

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Assistants)
admin.site.register(Student)