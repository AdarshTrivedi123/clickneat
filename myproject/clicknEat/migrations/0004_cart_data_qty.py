# Generated by Django 4.2.3 on 2023-07-19 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clicknEat', '0003_cart_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_data',
            name='qty',
            field=models.IntegerField(null=True),
        ),
    ]
