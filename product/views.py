from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Product, Category
from .serializers import ProductSerializer, CreateProductSerializer, CategorySerializer


class CreateProductAPI(CreateAPIView):
    serializer_class = CreateProductSerializer
    permission_classes = [IsAuthenticated]


class CreateCategoryAPI(CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class ListProductAPI(ListAPIView):
    queryset = Product.objects.filter(quantity__gt=0)
    serializer_class = ProductSerializer

class RetrieveProductAPI(RetrieveAPIView):
    queryset = Product.objects.filter(quantity__gt=0)
    serializer_class = ProductSerializer
    lookup_field = 'id'

class ListCategoryAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
