# Generated by Django 5.0.1 on 2024-02-02 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0007_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена за штуку'),
        ),
    ]
