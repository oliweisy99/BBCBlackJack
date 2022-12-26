from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField("Name", max_length=50, blank=True, null=True)
    score = models.IntegerField(default=0, blank=True,null=True)