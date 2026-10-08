from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Purchase,Stock
from ..serializers import PurchaseSerializer
from drf_spectacular.utils import extend_schema


class PurchaseListCreateView(GenericAPIView):
    def get(self, request):
        purchase=Purchase.objects.all()
        serializer= PurchaseSerializer(purchase, many=True)
        return Response(serializer.data)
   
    @extend_schema(request=PurchaseSerializer, responses= PurchaseSerializer)
    def post(self, request):
        serializer=PurchaseSerializer(data=request.data)
        
        if serializer.is_valid():
            purchase=serializer.save()
            
            stock,created=Stock.objects.get_or_create(product=purchase.product)
            stock.quantity +=purchase.quantity
            
            stock.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseDetailView(GenericAPIView):  
    def get(self, request, pk):
        try:
            purchase=Purchase.objects.get(pk=pk)
        except Purchase.DoesNotExist:
            return Response({'error':'purchase not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer=PurchaseSerializer(purchase)
        return Response(serializer.data)
        
    @extend_schema(request=PurchaseSerializer, responses= PurchaseSerializer)
    def put(self,request, pk):
        try:
            purchase= Purchase.objects.get(pk=pk)
        except Purchase.DoesNotExist:
            return Response({'error':'purchase not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer= PurchaseSerializer(purchase, data= request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            purchase=Purchase.objects.get(pk=pk)
        except Purchase.DoesNotExist:
            return Response({'error':'purchase not found'}, status= status.HTTP_404_NOT_FOUND)
        
        purchase.delete()
        
        return Response({'message':'purchase deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
