from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Stock
from ..serializers import StockSerializer
from drf_spectacular.utils import extend_schema


class StockListCreateView(GenericAPIView):
    def get(self, request):
        stock=Stock.objects.all()
        serializer= StockSerializer(stock, many=True)
        return Response(serializer.data)

    @extend_schema(request=StockSerializer, responses= StockSerializer)
    def post(self, request):
        serializer=StockSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StockDetailView(GenericAPIView): 
    def get(self, request, pk):
        try:
            stock=Stock.objects.get(pk=pk)
        except Stock.Doesnotexist:
            return Response({'error':'Stock not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer= StockSerializer(stock)
        return Response(serializer.data)
    
    
    @extend_schema(request=StockSerializer, responses= StockSerializer)
    def put(self, request, pk):
        try:
            stock= Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            return Response({'error':'stock not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer= StockSerializer(stock, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request, pk):
        try:
            stock=Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            return Response({'error':'stock not found'}, status= status.HTTP_404_NOT_FOUND)
        
        stock.delete()
        
        return Response({'message':'Stock deleted successfully'}, status=status.HTTP_204_NO_CONTENT)