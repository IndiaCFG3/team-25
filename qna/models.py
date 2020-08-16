from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ClassRoom(models.Model):
    name = models.CharField(max_length=100, null=False)
    class_id = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name


