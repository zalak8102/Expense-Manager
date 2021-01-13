from django.db import models

# Create your models here.

class user_details(models.Model):
    email = models.EmailField(max_length=30,primary_key=True)
    password = models.CharField(max_length=12, null=False)
    username = models.CharField(max_length=12)
    bdate = models.DateField()
    gender = models.CharField(max_length=6)
    