from django.contrib import admin
from .models import *


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'location', 'employee_count', 'owner', 'created', 'is_active')
    list_filter = ('location','is_active')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'skills')

@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    list_filter = ('company',)
    list_display = ('employee', 'company', 'post', 'is_active')