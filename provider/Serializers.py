from rest_framework import serializers
from .models import Provider, Auction

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'user']

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ['id', 'provider', 'title', 'description', 'start_time', 'end_time', 'price', 'is_active']
