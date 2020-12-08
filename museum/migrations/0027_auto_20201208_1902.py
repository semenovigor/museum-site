# Generated by Django 3.1.3 on 2020-12-08 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0026_guest_descriptiontext'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namePurpose', models.CharField(max_length=100, verbose_name='Название Цели')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='FIO',
            field=models.TextField(default='', verbose_name='ФИО ответственного'),
        ),
        migrations.AddField(
            model_name='event',
            name='countUser',
            field=models.IntegerField(default='', verbose_name='Количество участников'),
        ),
        migrations.AddField(
            model_name='event',
            name='mail',
            field=models.EmailField(default='', max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AddField(
            model_name='event',
            name='phone',
            field=models.CharField(default='', max_length=20, verbose_name='контактный телефон'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(verbose_name='Конец экскурсии'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(verbose_name='Начало экскурсии'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(default='', max_length=200, verbose_name='Название организации'),
        ),
        migrations.AddField(
            model_name='event',
            name='purpose',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='museum.purpose'),
        ),
    ]