# Generated by Django 4.1.4 on 2023-02-27 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_shoping_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
