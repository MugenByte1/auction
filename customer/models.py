from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)


class Offer(models.Model):
    price = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

