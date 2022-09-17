from pms.models import Department, Employee, Project
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields ="__all__"

class EmployeeSerializer(ModelSerializer):
    department_name= SerializerMethodField(read_only=True)

    def get_department_name(self, instance):
        return instance.department.name
    class Meta:
        model = Employee
        fields =("name", "email", "doj", "department_name")


class ProjectSerializer(ModelSerializer):
    employees = EmployeeSerializer(many=True,read_only=True)
    project_manager_name = SerializerMethodField(read_only=True)
    project_manager_email = SerializerMethodField(read_only=True)

    class Meta:
        model =Project
        fields = ("name", "start_date", "end_date", "project_manager_name", "project_manager_email", "employees")

    def get_project_manager_name(self, instance):
        return instance.project_manager.name

    def get_project_manager_email(self, instance):
        return instance.project_manager.email