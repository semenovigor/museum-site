# Generated by Django 3.1.3 on 2020-11-10 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0008_auto_20201109_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateTimeField(verbose_name='Дата Публикации'),
        ),
    ]