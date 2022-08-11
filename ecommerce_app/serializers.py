from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields=(
            'id',
            'title'
        )
        model = Category
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'category',
            'author',
            'isbn',
            'pages',
            'price',
            'stock',
            'description',
            'imageUrl',
            'status',
            'date_created'
        )
        model = book
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'product_tag',
            'name',
            'category',
            'price',
            'stock',
            'imageUrl',
            'status',
            'date_created'
        )
        model = Product
        

