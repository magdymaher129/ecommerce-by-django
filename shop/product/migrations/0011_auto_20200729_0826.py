# Generated by Django 3.0.5 on 2020-07-29 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20200729_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantaty',
            field=models.IntegerField(),
        ),
    ]