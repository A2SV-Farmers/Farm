# Generated by Django 4.1.7 on 2023-09-03 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('farm', '0002_remove_farmimage_farm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='farms', to='product.product'),
        ),
    ]