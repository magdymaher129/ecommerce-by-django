# Generated by Django 3.0.5 on 2020-07-27 23:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20200726_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
