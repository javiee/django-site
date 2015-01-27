from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.ManyToManyField(User)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Education(models.Model):

    user = models.ManyToManyField(User)
    school_name =  models.CharField(max_length=20) 
    field_study =  models.CharField(max_length=20)
    degree =  models.CharField(max_length=20)
    start_date =  models.CharField(max_length=20)
    end_date =  models.CharField(max_length=20)

class Positions(models.Model):

    user = models.ManyToManyField(User)
    title =  models.CharField(max_length=20)
    company =  models.CharField(max_length=20)
    summary =  models.TextField()
    is_current =  models.SmallIntegerField()
    start_date_year =  models.CharField(max_length=20)
    start_date_month =  models.CharField(max_length=20)
    end_date_year=  models.CharField(max_length=20)
    end_date_month =  models.CharField(max_length=20)

class Certifications(models.Model):

    user = models.ManyToManyField(User)
    name = models.CharField(max_length=20)
