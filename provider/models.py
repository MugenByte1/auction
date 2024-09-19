from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username





class Auction(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.FloatField()
    is_active = models.BooleanField(default=True)

    

    def is_active(self):
        return self.end_time > timezone.now()
    
    

