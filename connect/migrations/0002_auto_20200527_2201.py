# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-05-27 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connect.Author')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pk']},
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connect.Post'),
        ),
    ]