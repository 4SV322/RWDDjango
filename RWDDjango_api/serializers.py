from rest_framework import serializers
from .models import Skills, Groups, Institutes, Admins, Supervisors


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['skillname']


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['groupname']


class InstitutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institutes
        fields = ['institutename']


class AdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = ['username', 'email']


class SupervisorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisors
        fields = ['supervisorname', 'email']


