from django.contrib import admin

from University.Apps.AcademyMgmt.models import *

# Register your models here.

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
