# Generated by Django 3.0.5 on 2020-04-18 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_product', '0004_auto_20200418_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productid',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='manage_product.Email', verbose_name='e-mail клиента'),
        ),
    ]
