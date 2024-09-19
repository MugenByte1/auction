from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Auction
from .serializers import AuctionSerializer

class CancelAuction(APIView):
    def post(self, request, pk):
        try:
            auction = Auction.objects.get(pk=pk)
        except Auction.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        auction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EndAuction(APIView):
    def post(self, request, pk):
        try:
            auction = Auction.objects.get(pk=pk)
        except Auction.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        auction.is_active = False
        auction.save()
        serializer = AuctionSerializer(auction)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ListAllAuctions(APIView):
    def get(self, request):
        auctions = Auction.objects.all()
        serializer = AuctionSerializer(auctions, many=True)
        return Response(serializer.data)
