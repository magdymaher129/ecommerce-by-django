# Generated by Django 3.0.5 on 2020-07-27 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20200728_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(related_name='orderItems', to='product.OrderItem'),
        ),
    ]