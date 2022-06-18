from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class PlanUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan,on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username + ' registered for ' + self.plan.name 
    


