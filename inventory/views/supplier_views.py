from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Supplier
from ..serializers import SupplierSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView


class SupplierListCreateView(GenericAPIView):
    def get(self, request):
        supplier= Supplier.objects.all()
        serializer= SupplierSerializer(supplier, many=True)
        return Response(serializer.data)
        
    @extend_schema(request=SupplierSerializer, responses= SupplierSerializer)    
    def post(self, request):
        serializer=SupplierSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SupplierDetailView(GenericAPIView): 
    
    def get(self, request, pk):
        try:
            supplier= Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response({'error':'supplier not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer= SupplierSerializer(supplier)
        return Response(serializer.data)
            
    @extend_schema(request=SupplierSerializer, responses= SupplierSerializer)
    def put(self,request, pk):
        try:
            supplier= Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response({'error':'supplier not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer= SupplierSerializer(supplier, data= request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(request, pk):
        try:
            supplier= Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response({'error':'supplier not found'}, status= status.HTTP_404_NOT_FOUND)
        
        supplier.delete()
        
        return Response({'message':'Supplier deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

