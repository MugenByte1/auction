from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *


class ListCreateOffer(ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def perform_create(self, serializer):
        if .auction.price >= self.price