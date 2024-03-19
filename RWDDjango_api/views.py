from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import (Groups,
                     Skills,
                     Institutes)
from .serializers import (GroupsSerializer,
                          SkillsSerializer,
                          InstitutesSerializer)

class GroupListView(APIView):
    def get(self, request, format=None):
        group = Groups.objects.all()
        serializer = GroupsSerializer(Groups, many=True)
        return Response(serializer.data)

class SkillListView(APIView):
    def get(self, request, format=None):
        skill = Skills.objects.all()
        serializer = SkillsSerializer(Skills, many=True)
        return Response(serializer.data)

class InstituteListView(APIView):
    def get(self, request, format=None):
        institute = Institutes.objects.all()
        serializer = InstitutesSerializer(institute, many=True)
        return Response(serializer.data)
