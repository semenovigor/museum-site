# Generated by Django 3.1.3 on 2020-11-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(blank=True, upload_to='media', verbose_name='Картинка'),
        ),
    ]