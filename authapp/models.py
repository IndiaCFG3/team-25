from django.db import models
from django.contrib.auth.models import User

# Create your models here.

@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
    
    if created :
        UserProfile.objects.create(user=instance)

        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    
    instance.userprofile.save()


class UserProfile(models.Model):  
    user = models.ForeignKey(User, unique=True)
    isTeacher = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, default="")
    subject = models.CharField(max_length=20, blank=True, null=True)