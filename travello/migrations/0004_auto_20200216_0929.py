# Generated by Django 3.0.2 on 2020-02-16 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_city_uploaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='uploaded',
            field=models.DateField(auto_now_add=True),
        ),
    ]
