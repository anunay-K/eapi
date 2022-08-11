from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.

class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class DetailsCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
class ListBook(generics.ListCreateAPIView):
    queryset = book.objects.all()
    serializer_class=BookSerializer
    
class DetailsBook(generics.RetrieveUpdateDestroyAPIView):
    queryset=book.objects.all()
    serializer_class=BookSerializer
    
class ListProducts(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
class DetailsProducts(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
       
