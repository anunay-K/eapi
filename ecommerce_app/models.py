from re import M
from tabnanny import verbose
from django.db import models

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=70)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title
    
class book(models.Model):
    title=models.CharField(max_length=100)
    category=models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    author= models.CharField(max_length=100, default='Anunay')
    isbn=models.CharField(max_length=10)
    pages=models.IntegerField()
    price=models.IntegerField()
    stock=models.IntegerField()
    description=models.TextField()
    imageUrl=models.URLField()
    status=models.BooleanField(default=True)
    date_created=models.DateField(auto_now_add=True)
    
    class Meta:
        ordering=['-date_created']
        
    def __str__(self):
        return self.title
    

class Product(models.Model):
    product_tag=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    price=models.IntegerField()
    stock=models.IntegerField()
    imageUrl=models.URLField()
    status=models.BooleanField(default=True)
    date_created=models.DateField(auto_now_add=True)
    
    class Meta:
        ordering=['-date_created']
    
    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)
    
    
    
    
    