# Generated by Django 4.1.7 on 2023-09-03 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='product_images',
            field=models.ManyToManyField(related_name='products', to='product.productimage'),
        ),
    ]
