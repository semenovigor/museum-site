# Generated by Django 3.1.3 on 2020-11-08 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0006_auto_20201109_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateTimeField(verbose_name='Дата Публикации'),
        ),
    ]