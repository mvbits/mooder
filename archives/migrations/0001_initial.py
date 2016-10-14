# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 16:10
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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='分类名')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': '分类',
                'verbose_name': '分类',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='名称')),
                ('link', models.URLField(verbose_name='链接')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': '应用链接',
                'verbose_name': '应用链接',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('verify', models.CharField(choices=[('wait', '待审核'), ('pass', '通过'), ('failed', '未通过')], default='wait', max_length=8, verbose_name='状态')),
                ('visible', models.CharField(choices=[('private', '私密的'), ('sell', '出售的'), ('public', '公开的')], default='private', max_length=8, verbose_name='公开度')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
                ('show', models.BooleanField(default=True, verbose_name='显示')),
                ('rank', models.PositiveIntegerField(blank=True, default=0, verbose_name='Rank')),
                ('level', models.CharField(choices=[('low', '低危'), ('medium', '中危'), ('high', '高危'), ('grave', '严重')], default='low', max_length=8, verbose_name='等级')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('verify_time', models.DateTimeField(blank=True, null=True, verbose_name='审核时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archives.Category', verbose_name='分类')),
            ],
            options={
                'ordering': ['-created_time'],
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
            },
        ),
    ]
