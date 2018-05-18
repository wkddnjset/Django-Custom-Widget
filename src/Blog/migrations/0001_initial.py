# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-18 04:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateField()),
                ('location', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('message', models.TextField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Country')),
            ],
        ),
    ]
