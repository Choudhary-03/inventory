from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Category
from ..serializers import CategorySerializer
from drf_spectacular.utils import extend_schema


class CategoryListCreateView(GenericAPIView):
    
    def get(self, request):
        category= Category.objects.all()
        serializer= CategorySerializer(category, many=True)
        return Response(serializer.data)
    
        
    @extend_schema(request=CategorySerializer, responses= CategorySerializer)
    def post(self, request):
        serializer=CategorySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(GenericAPIView):
    
    def get(self, request, pk):
        try:
            category= Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error':"category not found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=CategorySerializer(category)
        return Response(serializer.data)
    
    @extend_schema(request=CategorySerializer, responses= CategorySerializer)
    def put(self, request, pk):
        try:
            category= Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error':'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer= CategorySerializer(category, data= request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        try:
            category= Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error':'category not found'}, status= status.HTTP_404_NOT_FOUND)
        
        category.delete()
        
        return Response({'message':'category deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
