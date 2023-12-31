from django.shortcuts import render
from rest_framework.views import APIView
from my_projects.models import Project
from my_projects.serializers import ProjectSerializers 
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class MyProjectView(APIView):
    def get(self ,request, id=None):
        try:
            if id is None:
                projects_details = Project.objects.all()
                projects_serializer = ProjectSerializers(projects_details, many=True, context={'request': request})
                return Response(projects_serializer.data, status=status.HTTP_200_OK)
            else:
                projects_details = Project.objects.get(id=id)
                projects_serializer = ProjectSerializers(projects_details, context={'request': request})
                return Response(projects_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print("Some Error Occured")
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        