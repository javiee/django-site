from django.db import models

class User(models.Model):

    user =  models.CharField(max_length=20)
    oauth_token_secret =  models.CharField(max_length=200)

class Profile(models.Model):
# Create your models here.
    user = models.ForeignKey(User)
    auth_token = models.CharField(max_length=200)
    auth_secret = models.CharField(max_length=200)


