# Generated by Django 3.0.5 on 2020-04-24 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_product', '0005_auto_20200418_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='productid',
            name='product_link',
            field=models.CharField(default='link', max_length=100, verbose_name='Ссылка на изделие'),
        ),
    ]
