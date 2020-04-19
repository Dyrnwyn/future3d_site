# Generated by Django 3.0.5 on 2020-04-15 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_product', '0002_auto_20200412_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='email@email.ru', max_length=254, unique=True, verbose_name='e-mail')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.AlterModelOptions(
            name='productid',
            options={'ordering': ['-template'], 'verbose_name': 'Изделие', 'verbose_name_plural': 'Изделия'},
        ),
        migrations.AddField(
            model_name='productid',
            name='date_close',
            field=models.DateField(null=True, verbose_name='Дата отправки заказа'),
        ),
        migrations.AddField(
            model_name='productid',
            name='date_opening',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата принятия заказа'),
        ),
        migrations.AddField(
            model_name='productid',
            name='date_payment',
            field=models.DateField(null=True, verbose_name='Дата оплаты'),
        ),
        migrations.AddField(
            model_name='productid',
            name='stage',
            field=models.CharField(choices=[('pay', 'Оплата'), ('in_work', 'Верстка'), ('perfomed', 'Выполнено')], default=1, max_length=10, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='productid',
            name='email',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='manage_product.Email'),
        ),
    ]