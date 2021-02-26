from django.db import models
from signup.models import user_details
# Create your models here.
class goal(models.Model):
    goalId = models.AutoField(primary_key=True)
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    goalName = models.CharField(max_length=20)
    amount = models.IntegerField()
    date = models.DateField()
    contribution = models.IntegerField()
    status = models.IntegerField()
    count = models.IntegerField(default=0)

class contribLog(models.Model):
    conId = models.AutoField(primary_key=True)
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    goal = models.ForeignKey(goal, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()

    
