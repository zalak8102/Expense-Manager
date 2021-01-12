from django.db import models
from signup.models import user_details
# Create your models here.
class income_details(models.Model):
    incomeID = models.AutoField(primary_key=True)
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=30)
    amount = models.IntegerField()
    date = models.DateField()
    regular = models.BooleanField()

