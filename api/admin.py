from django.contrib import admin
from api.models import Employee,Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','location','type')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','address','comapany')
# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)