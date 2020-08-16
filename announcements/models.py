from django.db import models
from qna.models import ClassRoom

# Create your models here.
class Announcements(models.Model):
    class_id = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    link = models.URLField(null=True, blank=True)
    body = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.class_id + " " + self.title[0:10] + "..."



