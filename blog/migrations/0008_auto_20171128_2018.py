# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 20:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_down_count'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([]),
        ),
    ]