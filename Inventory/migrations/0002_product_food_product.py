# Generated by Django 4.2.10 on 2024-02-24 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='food_product',
            field=models.BooleanField(default=False),
        ),
    ]
