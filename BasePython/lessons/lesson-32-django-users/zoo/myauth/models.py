from django.contrib.auth.models import User, AbstractUser
from django.db import models


# extend example via 1:1
# class MyUserProfile(models.Model):
#     user = models.OneToOneField(User,
#                                 on_delete=models.CASCADE,
#                                 primary_key=True)

#     avatar = models.ImageField(upload_to='avatar', blank=True)
#     b_year = models.PositiveIntegerField(null=True)


class MyUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', blank=True)
    b_year = models.PositiveIntegerField(null=True)

