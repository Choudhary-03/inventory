from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from ..models import Product
from ..serializers import ProductSerializer
from drf_spectacular.utils import extend_schema


class ProductListCreateView(GenericAPIView):
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser, FormParser]

    @extend_schema(responses=ProductSerializer)
    def get(self, request):
        products = Product.objects.all()
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=ProductSerializer,
        responses=ProductSerializer
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        ) 
    
class ProductDetailView(GenericAPIView):
    parser_classes=[MultiPartParser,FormParser]
    def get(self, request,pk):
        try:
            product=Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error':'product not found'},status=status.HTTP_404_NOT_FOUND)

        serializer= ProductSerializer(product)
        return Response(serializer.data)

    @extend_schema(request= ProductSerializer, responses= ProductSerializer)    
    def put(self, request, pk):
        try:
            product= Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error':'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer= ProductSerializer(product, data= request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            product= Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error':'product not found'}, status= status.HTTP_404_NOT_FOUND)
        
        product.delete()
        return Response({'message':'product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    