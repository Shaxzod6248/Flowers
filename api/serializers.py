from rest_framework import serializers
from products.models import *
from users.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class Flowerserializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class Order_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_detail
        fields = '__all__'