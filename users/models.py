from django.db import models


# Create your models here.

# CharField
# BooleanField
# DateTimeField
# EmailField
# IntegerField
# TextField
# URLField


class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


# profile = UserProfile.objects.get(user__email='nitesh@gmail.com')

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, related_name='profile')
    profile_pic_url = models.CharField(max_length=255, default="")
    bio = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
