# Generated by Django 3.1.3 on 2020-12-07 11:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0025_auto_20201204_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='descriptionText',
            field=ckeditor.fields.RichTextField(default=' ', verbose_name='Отзыв Гостя'),
        ),
    ]