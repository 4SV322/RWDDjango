from django.db import models
from django.contrib.auth.models import User


class Projects(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    paid = models.BooleanField(default=False)
    goal = models.TextField()
    workcond = models.TextField()


class Admins(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)


class Institutes(models.Model):
    institutename = models.CharField(max_length=255)


class Groups(models.Model):
    groupname = models.CharField(max_length=255)


class Posts(models.Model):
    name = models.CharField(max_length=255)


class State(models.Model):
    name = models.CharField(max_length=255)
# 0 - disable
# 1 - active
# 2 - waiting


class Skills(models.Model):
    name = models.CharField(max_length=255, unique=True)
    stateId = models.BigIntegerField(default=3)


class Vacancies(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    dateStart = models.DateField()
    dateEnd = models.DateField()
    conditions = models.TextField()
    duties = models.TextField()
    requirements = models.TextField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)


class Users(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # institute = models.ForeignKey(Institutes, on_delete=models.CASCADE)
    # group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    # posts = models.ForeignKey(Posts, on_delete=models.CASCADE)
    # skills = models.ForeignKey(Skills, on_delete=models.CASCADE)
    # vacancies = models


class Supervisors(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)


class ProjectSkills(models.Model):
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)


class VacanciesSkills(models.Model):
    vacancy = models.ForeignKey(Vacancies, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)