# Generated by Django 4.1.7 on 2023-03-12 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_brand_product_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]
