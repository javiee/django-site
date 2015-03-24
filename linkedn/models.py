from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class Education(models.Model):

    user = models.ForeignKey(User)
    school_name =  models.CharField(max_length=100) 
    field_study =  models.CharField(max_length=100)
    summary = models.TextField(default= None)
    degree =  models.CharField(max_length=100)
    start_date =  models.CharField(max_length=20)
    end_date =  models.CharField(max_length=20)

    def __str__(self):
        return self.field_study

class Positions(models.Model):

    user = models.ForeignKey(User)
    title =  models.CharField(max_length=100)
    company =  models.CharField(max_length=100)
    summary =  models.TextField(null = True)
    is_current =  models.CharField(max_length=20)
    start_date_year =  models.CharField(max_length=20)
    start_date_month =  models.CharField(max_length=20)
    end_date_year=  models.CharField(max_length=20, blank = True)
    end_date_month =  models.CharField(max_length=20, blank = True)

    def __str__(self):
        return self.title

class Certifications(models.Model):

    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Skill(models.Model):
    user = models.ForeignKey(User)
    skill_name =  models.CharField(max_length=150)
    def __str__(self):
        return self.skill_name
