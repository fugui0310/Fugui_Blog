# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.core.validators
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='username', max_length=30, unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], error_messages={'unique': 'A user with that username already exists.'})),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=254, blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(verbose_name='昵称', max_length=32)),
                ('telephone', models.CharField(verbose_name='手机号码', max_length=11, unique=True, blank=True, null=True)),
                ('avatar', models.FileField(verbose_name='头像', default='/avatar/default.png', upload_to='avatar')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('groups', models.ManyToManyField(verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='文章标题', max_length=50)),
                ('desc', models.CharField(verbose_name='文章描述', max_length=255)),
                ('read_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('up_count', models.IntegerField(default=0)),
                ('down_count', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('article_type_id', models.IntegerField(default=None, choices=[(1, '编程语言'), (2, '软件设计'), (3, '前端'), (4, '操作系统'), (5, '数据库')])),
            ],
        ),
        migrations.CreateModel(
            name='Article2Tag',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('article', models.ForeignKey(verbose_name='文章', to='blog.Article')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleDetail',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='文章内容')),
                ('article', models.OneToOneField(verbose_name='所属文章', to='blog.Article')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleUp',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('article', models.ForeignKey(null=True, to='blog.Article')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='个人博客标题', max_length=64)),
                ('site', models.CharField(verbose_name='个人博客后缀', max_length=32, unique=True)),
                ('theme', models.CharField(verbose_name='博客主题', max_length=32)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='分类标题', max_length=32)),
                ('blog', models.ForeignKey(verbose_name='所属博客', to='blog.Blog')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'category',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(verbose_name='评论内容', max_length=255)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('up_count', models.IntegerField(default=0)),
                ('article', models.ForeignKey(verbose_name='评论文章', to='blog.Article')),
                ('parent_comment', models.ForeignKey(verbose_name='父级评论', blank=True, null=True, to='blog.Comment')),
                ('user', models.ForeignKey(verbose_name='评论者', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentUp',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.ForeignKey(null=True, to='blog.Comment')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='标签名称', max_length=32)),
                ('blog', models.ForeignKey(verbose_name='所属博客', to='blog.Blog')),
            ],
        ),
        migrations.AddField(
            model_name='article2tag',
            name='tag',
            field=models.ForeignKey(verbose_name='标签', to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='文章类型', null=True, to='blog.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', through='blog.Article2Tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(verbose_name='所属用户', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='article2tag',
            unique_together=set([('article', 'tag')]),
        ),
    ]
