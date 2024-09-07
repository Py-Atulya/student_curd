from django.contrib import admin
from .models import Student


class studentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'first_name', 'last_name', 'email','phone_number','address')

admin.site.register(Student, studentAdmin)