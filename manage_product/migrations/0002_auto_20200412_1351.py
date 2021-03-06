# Generated by Django 3.0.5 on 2020-04-12 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productid',
            name='img',
            field=models.ImageField(upload_to='img/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='productid',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='Оплачено'),
        ),
        migrations.AlterField(
            model_name='productid',
            name='payment_id',
            field=models.CharField(max_length=10, verbose_name='id оплаты'),
        ),
        migrations.AlterField(
            model_name='productid',
            name='template',
            field=models.CharField(choices=[('1527', '1527'), ('2032', '2032'), ('2104', '2104'), ('4021', '4021'), ('4030', '4030')], max_length=4, verbose_name='Номер шаблона'),
        ),
    ]
