# Generated by Django 3.1.3 on 2020-12-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0029_auto_20201208_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='phone',
            field=models.CharField(default='', max_length=20, verbose_name='контактный телефон'),
        ),
    ]
