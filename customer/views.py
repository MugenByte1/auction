from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from provider.models import *
from provider.Serializers import *
from django.http.response import HttpResponse
from datetime import timedelta

class ListCreateOffer(ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def perform_create(self, serializer):
        auction = Auction.objects.get(id = serializer.validated_data['auction'])
        price = serializer.validated_data['price']
        if auction.price >= price:
            raise ValueError('price invalid')
        else:
            auction.start_time += timedelta(minutes=10)
            auction.save()
            return super().perform_create(serializer)
