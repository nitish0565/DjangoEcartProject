from django.db import models


class Drinks(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name +" "+self.description


class Products(models.Model):
    productname = models.CharField(max_length=500)
    productcategory = models.CharField(max_length=100)
    ratings = models.IntegerField()
    price = models.IntegerField()
    created_datetime = models.DateTimeField(auto_now=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    productimage = models.TextField(max_length=500,default="https://www.shutterstock.com/image-illustration/bottle-gel-lotion-beauty-product-260nw-1348122737.jpg")


