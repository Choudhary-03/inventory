from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Sale, Product, Stock
from ..serializers import SaleSerializer
from drf_spectacular.utils import extend_schema
from django.db import transaction

class SaleListView(GenericAPIView):

    def get(self, request):
        sale=Sale.objects.all()
        serializer= SaleSerializer(sale, many=True)
        return Response(serializer.data)


class SaleCreateView(GenericAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    @extend_schema(request=SaleSerializer, responses=SaleSerializer)
    def post(self, request):
        serializer = SaleSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']

        with transaction.atomic():
            try:
                stock = Stock.objects.select_for_update().get(product=product)
            except Stock.DoesNotExist:
                return Response(
                    {'error': 'Stock not found for this product'},
                    status=status.HTTP_404_NOT_FOUND
                )

            if stock.quantity < quantity:
                return Response(
                    {'error': 'Insufficient stock'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            sale = serializer.save()
            stock.quantity -= sale.quantity
            stock.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SaleDetailView(GenericAPIView):
    
    def get(self, request, pk):
        try:
            sale=Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            return Response({'error':'sale not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer= SaleSerializer(sale)
        return Response(serializer.data)
            
    @extend_schema(request=SaleSerializer, responses= SaleSerializer)
    def put(self,request, pk):
        try:
            sale= Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            return Response({'error':'sale not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=SaleSerializer(sale, data= request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #DELETE
    def delete(self, request, pk):
        try:
            sale=Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            return Response({'error':'sale not found'}, status= status.HTTP_404_NOT_FOUND)
        
        sale.delete()
        return Response({'message':'Sale deleted successfully'}, status=status.HTTP_204_NO_CONTENT)