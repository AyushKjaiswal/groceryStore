from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100 , blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args,**kwargs)

    def __str__(self):
        return self.category_name
    
class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    def __str__(self):
        return self.color_name
    

class QuantityVariant(models.Model):
    quantity_name = models.CharField(max_length=100)

    def __str__(self):
        return self.quantity_name
    

class SizeVariant(models.Model):
    size_name = models.CharField(max_length=100)

    def __str__(self):
        return self.size_name
    



class Products(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    products_name = models.CharField(max_length=100)
    images = models.ImageField(upload_to='static/images')
    price = models.CharField(max_length=100)
    description = models.TextField()
    stock = models.IntegerField(default=100)

    quantity = models.ForeignKey(QuantityVariant,on_delete=models.PROTECT,blank=True,null=True)
    color = models.ForeignKey(ColorVariant,on_delete=models.PROTECT,blank=True,null=True)
    size = models.ForeignKey(SizeVariant,on_delete=models.PROTECT,blank=True,null=True)


    def __str__(self):
        return self.products_name
    
class ProductImages(models.Model):
    product_image = models.ForeignKey(Products,on_delete=models.PROTECT)
    images = models.ImageField(upload_to='static/images')
    

