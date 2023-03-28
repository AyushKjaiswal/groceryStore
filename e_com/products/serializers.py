from rest_framework import serializers
from .models import *
  



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class QuantitySerializers(serializers.ModelSerializer):
    class Meta:
        model = QuantityVariant
        fields = '__all__'


class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = ColorVariant
        fields = '__all__'


class SizeSerializers(serializers.ModelSerializer):
    class Meta:
        model = SizeVariant
        fields = '__all__'



class ProductSeriallizers(serializers.ModelSerializer):
    category = CategorySerializers()
    quantity = QuantitySerializers()
    color = ColorVariant()
    size = SizeVariant()

    class Meta:
        model = Products
        fields = '__all__'
        # exclude = ['id']


