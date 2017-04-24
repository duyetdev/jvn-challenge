# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 05:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=250, verbose_name='Competition title')),
                ('content', models.TextField(verbose_name='Competition content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('add_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompetitionDataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200, verbose_name='File name')),
                ('file_path', models.CharField(max_length=200)),
                ('file_size', models.CharField(max_length=200, verbose_name='File size')),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='datasets',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competition.CompetitionDataset'),
        ),
    ]