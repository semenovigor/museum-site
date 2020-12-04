# Generated by Django 3.1.3 on 2020-11-07 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCategory', models.CharField(max_length=100, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название новости')),
                ('text', models.TextField(verbose_name='Описание Новости')),
                ('image', models.ImageField(upload_to='media', verbose_name='Картинка')),
                ('date', models.DateTimeField(verbose_name='Дата Публикации')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='museum.category')),
            ],
        ),
    ]