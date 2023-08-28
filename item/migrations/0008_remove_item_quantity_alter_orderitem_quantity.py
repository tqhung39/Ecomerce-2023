# Generated by Django 4.2.4 on 2023-08-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]