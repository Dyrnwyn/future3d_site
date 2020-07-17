# Generated by Django 3.0.5 on 2020-05-12 12:49

from django.db import migrations, models
import django.db.models.deletion
import manage_product.models


class Migration(migrations.Migration):

    replaces = [('manage_product', '0002_auto_20200412_1351'), ('manage_product', '0003_auto_20200415_1517'), ('manage_product', '0004_auto_20200418_2240'), ('manage_product', '0005_auto_20200418_2243'), ('manage_product', '0006_productid_product_link'), ('manage_product', '0007_auto_20200508_2302'), ('manage_product', '0008_auto_20200509_2247'), ('manage_product', '0009_auto_20200509_2256'), ('manage_product', '0010_auto_20200509_2327'), ('manage_product', '0011_auto_20200509_2328'), ('manage_product', '0012_auto_20200512_1942')]

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
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='email@email.ru', max_length=254, verbose_name='e-mail')),
            ],
            options={
                'verbose_name': 'Электронные почты',
                'verbose_name_plural': 'электронная почта',
            },
        ),
        migrations.AlterModelOptions(
            name='productid',
            options={'ordering': ['-template'], 'verbose_name': 'Изделие', 'verbose_name_plural': 'Изделия'},
        ),
        migrations.AddField(
            model_name='productid',
            name='date_opening',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата принятия заказа'),
        ),
        migrations.AddField(
            model_name='productid',
            name='date_close',
            field=models.DateField(blank=True, null=True, verbose_name='Дата отправки заказа'),
        ),
        migrations.AddField(
            model_name='productid',
            name='date_payment',
            field=models.DateField(blank=True, null=True, verbose_name='Дата оплаты'),
        ),
        migrations.AlterField(
            model_name='productid',
            name='img',
            field=models.ImageField(upload_to=manage_product.models.ProductId.upload_path, verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='productid',
            name='stage',
            field=models.CharField(choices=[('new', 'Новый'), ('pay', 'Оплата'), ('in_work', 'Верстка'), ('perfomed', 'Выполнено')], default=1, max_length=10, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='productid',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='manage_product.Email', verbose_name='e-mail клиента'),
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town', models.CharField(max_length=50, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.AlterField(
            model_name='productid',
            name='img',
            field=models.ImageField(null=True, upload_to=manage_product.models.ProductId.upload_path, verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='productid',
            name='organisation',
            field=models.CharField(choices=[('school', 'Школа'), ('playschool', 'Детский сад')], default=1, max_length=100, verbose_name='Учебное заведение'),
        ),
        migrations.AlterField(
            model_name='productid',
            name='payment_id',
            field=models.CharField(default=manage_product.models.ProductId.generate_pay_id, max_length=10, verbose_name='id оплаты'),
        ),
        migrations.AlterField(
            model_name='productid',
            name='payment_id',
            field=models.CharField(default=manage_product.models.ProductId.generate_pay_id, max_length=10, unique=True, verbose_name='id оплаты'),
        ),
        migrations.AddField(
            model_name='productid',
            name='img_jpg',
            field=models.ImageField(blank=True, null=True, upload_to=manage_product.models.ProductId.upload_path, verbose_name='Фото для скачивания'),
        ),
        migrations.AddField(
            model_name='productid',
            name='organisation_name',
            field=models.CharField(blank=True, default='1', max_length=50, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='productid',
            name='payment_id',
            field=models.CharField(default=manage_product.models.ProductId.generate_pay_id, max_length=10, verbose_name='id оплаты'),
        ),
        migrations.AddField(
            model_name='productid',
            name='town',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='manage_product.Town', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='productid',
            name='worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='manage_product.Worker', verbose_name='Менеджер'),
        ),
        migrations.AlterField(
            model_name='productid',
            name='payment_id',
            field=models.CharField(default=manage_product.models.ProductId.generate_pay_id, max_length=10, unique=True, verbose_name='id оплаты'),
        ),
        migrations.AlterField(
            model_name='productid',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=manage_product.models.ProductId.upload_path, verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='productid',
            name='product_link',
            field=models.CharField(blank=True, default='link', max_length=100, verbose_name='Ссылка на изделие'),
        ),
    ]
