# Generated by Django 4.2.2 on 2023-06-11 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='productimage',
            field=models.TextField(default='https://www.shutterstock.com/image-illustration/bottle-gel-lotion-beauty-product-260nw-1348122737.jpg', max_length=500),
        ),
    ]