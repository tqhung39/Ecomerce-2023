# Generated by Django 4.2.4 on 2023-08-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',), 'verbose_name_plural': 'Items'},
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(blank=True),
        ),
    ]
