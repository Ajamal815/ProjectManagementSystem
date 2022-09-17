
from django.contrib import admin
from django.urls import path
from pms.views import get_projects
urlpatterns = [
    path('admin/', admin.site.urls),
    path("projects/", get_projects),
]
