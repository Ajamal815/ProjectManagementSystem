from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    doj = models.DateField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE, related_name="employee_department")

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    project_manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="manager")
    employees = models.ManyToManyField(Employee, related_name="assign_to")

    def __str__(self):
        return self.name