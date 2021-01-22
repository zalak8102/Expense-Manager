from django.db import models
from signup.models import user_details
# Create your models here.
class expense(models.Model):
    expId=models.AutoField(primary_key=True)
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    expName=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    amount = models.IntegerField()
    date = models.DateField()
    comments=models.CharField(max_length=100)
