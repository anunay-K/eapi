from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('categories',ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/',DetailsCategory.as_view(), name='singlecategory'),
    path('books', ListBook.as_view(),name='books'),
    path('books/<int:pk>/', DetailsBook.as_view(), name='singlebook'),
    
    path('products', ListProducts.as_view(), name='products'),
    path('products/<int:pk>/',DetailsProducts.as_view(), name='singleproduct')
]