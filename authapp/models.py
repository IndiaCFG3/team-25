from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from qna.models import ClassRoom

# Create your models here.

@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
    
    if created :
        UserProfile.objects.create(user=instance)

        



class UserProfile(models.Model): 
    user = models.ForeignKey(User, on_delete =models.CASCADE, related_name="user")
    isTeacher = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, default="")
    subject = models.CharField(max_length=20, blank=True, null=True)
    classroom = models.ForeignKey(ClassRoom, related_name="classroom", on_delete=models.CASCADE)
    isFeaturePhone = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
        