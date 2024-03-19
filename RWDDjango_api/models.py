from django.db import models
from django.contrlib.auth.models import User

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

class Skills(models.Model):
    skillname = models.CharField(max_length=255)

class Vacancies(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    datestart = models.DateField()
    dateend = models.DateField()
    conditions = models.TextField()
    duties = models.TextField()
    requirements = models.TextField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

class Users(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    #institute = models.ForeignKey(Institutes, on_delete=models.CASCADE)
    #group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    #posts = models.ForeignKey(Posts, on_delete=models.CASCADE)
    #skills = models.ForeignKey(Skills, on_delete=models.CASCADE)
    #vacancies = models

class Supervisors(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)


