from django.http import JsonResponse
from .models import Drinks, Products
from .serializer import DrinkSerializer, ProdcutsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def drink_list(request,format=None):
    if request.method == 'GET':
        drinks = Drinks.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def product(request,format=None):
    if request.method == "GET":
        products = Products.objects.all()
        productsserializer = ProdcutsSerializer(products, many=True)
        return JsonResponse(productsserializer.data, safe=False)

    if request.method == "POST":
        products_serializer = ProdcutsSerializer(data=request.data)
        if products_serializer.is_valid():
            products_serializer.save()
            return Response(products_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error_msg":"not a valid param passed"},status=status.HTTP_204_NO_CONTENT)


@api_view(["GET","PUT","DELETE"])
def product_details(request,id,format=None):
    try:
        products=Products.objects.get(pk=id)
    except Products.DoesNotExist:
        return Response({"msg":"product not found"},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        product_serializer= ProdcutsSerializer(products)
        return Response(product_serializer.data)

    elif request.method == "PUT":
        product_serializer= ProdcutsSerializer(products, request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




