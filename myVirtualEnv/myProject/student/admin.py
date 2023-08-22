from django.contrib import admin
from .models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ("fname", "lname", "phone", "dob")


admin.site.register(Student, StudentAdmin)
