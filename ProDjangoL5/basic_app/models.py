from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):
    # create relationship (don`t inherit from User)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additioanal attributes you want
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='portfolio', blank=True)
    # user_nick = models.CharField(max_length=256, name='UserNick', unique=True)

    def __str__(self):
        # Built-in attribute to django.contrib.auth.models.User
        return self.user.username
