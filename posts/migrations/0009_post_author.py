# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170302_1644'),
        ('posts', '0008_remove_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='users.User', verbose_name='User'),
            preserve_default=False,
        ),
    ]
