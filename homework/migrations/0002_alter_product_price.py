# Generated by Django 5.0.1 on 2024-02-02 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена за штуку'),
        ),
    ]
