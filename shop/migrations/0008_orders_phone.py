# Generated by Django 4.1.4 on 2023-03-11 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orders_alter_contact_desc_alter_contact_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
    ]
