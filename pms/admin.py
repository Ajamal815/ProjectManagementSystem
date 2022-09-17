from django.contrib import admin

# Register your models here.
from .models import Employee, Project, Department
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Project)