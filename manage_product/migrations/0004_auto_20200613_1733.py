# Generated by Django 3.0.5 on 2020-06-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_product', '0003_fotoorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True, verbose_name='Инструкция')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.RemoveField(
            model_name='fotoorder',
            name='description',
        ),
    ]
