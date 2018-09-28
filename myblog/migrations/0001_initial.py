# Generated by Django 2.1.1 on 2018-09-26 03:32

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
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('content', models.TextField(default='', verbose_name='内容')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2018, 9, 26, 3, 32, 22, 158205, tzinfo=utc), verbose_name='创建时间')),
                ('flash_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击率')),
            ],
            options={
                'verbose_name': '我的文章',
                'verbose_name_plural': '我的文章',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='文章类别')),
            ],
            options={
                'verbose_name': '文章类别',
                'verbose_name_plural': '文章类别',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='文章标签')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.Category', verbose_name='文章类别'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(to='myblog.Tag', verbose_name='文章标签'),
        ),
    ]
