from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.TextField()
    file = models.FileField(upload_to="resources/", null=True, blank=True)
    url = models.URLField(blank=True, null=True)
