from django.contrib import admin
from .models import Employees

@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department', 'salary')
    search_fields = ('name', 'email', 'department')
