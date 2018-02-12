# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-02-12 03:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('url', models.URLField(default='http://i.imgur.com/Ous4iGB.png')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Maker')),
            ],
        ),
        migrations.CreateModel(
            name='PPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='产品照片', max_length=20)),
                ('url', models.URLField(default='http://i.imgur.com/z230eeq.png')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='超值手机', max_length=15)),
                ('description', models.TextField(default='暂无说明')),
                ('year', models.PositiveIntegerField(default=2016)),
                ('price', models.PositiveIntegerField(default=0)),
                ('pmodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.PModel')),
            ],
        ),
        migrations.AddField(
            model_name='pphoto',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Product'),
        ),
    ]
