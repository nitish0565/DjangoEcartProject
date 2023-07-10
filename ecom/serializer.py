from rest_framework import serializers
from .models import Drinks, Products


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = '__all__'
        # fied =('id','name','description')


class ProdcutsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
