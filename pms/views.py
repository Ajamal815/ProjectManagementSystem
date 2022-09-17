from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer
# Create your views here.

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_projects(request):
    page = request.query_params.get("p",1)
    projects = Project.objects.all()
    paginator = Paginator(projects, 1)
    paginated_response = paginator.get_page(page)
    return Response({"result":{"data":ProjectSerializer(paginated_response, many=True).data,"page":page, 'pageSize':paginator.num_pages, "hasMore":paginated_response.has_next(),"totalItems":projects.count()}}, status=status.HTTP_200_OK)