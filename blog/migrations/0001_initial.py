# Generated by Django 2.1.1 on 2018-09-25 06:00

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名前')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 9, 25, 6, 0, 49, 174810, tzinfo=utc), verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='本文')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 9, 25, 6, 0, 49, 201792, tzinfo=utc), verbose_name='作成日')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Category', verbose_name='カテゴリー')),
            ],
        ),
    ]
