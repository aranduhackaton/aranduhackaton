# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-16 21:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('arandusite', '0004_auto_20160416_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itembase_related', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='learninglist',
            name='items',
        ),
        migrations.RemoveField(
            model_name='learningvideo',
            name='item',
        ),
        migrations.AddField(
            model_name='learningvideo',
            name='learning_list',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='arandusite.LearningList'),
            preserve_default=False,
        ),
    ]
