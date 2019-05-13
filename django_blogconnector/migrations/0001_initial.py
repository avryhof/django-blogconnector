# Generated by Django 2.2.1 on 2019-05-10 14:49

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
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('syndication_type', models.CharField(blank=True, max_length=16, null=True)),
                ('syndication_link', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('last_build_date', models.DateTimeField(blank=True, null=True)),
                ('language', models.CharField(blank=True, default='en-us', max_length=20, null=True)),
                ('update_period', models.CharField(blank=True, default='hourly', max_length=20, null=True)),
                ('update_frequency', models.CharField(blank=True, default='1', max_length=8, null=True)),
                ('blog_type', models.CharField(blank=True, default='WordPress', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('blog_username', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('guid', models.CharField(blank=True, max_length=255, null=True)),
                ('guid_is_permalink', models.BooleanField(default=False)),
                ('blog_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='django_blogconnector.BlogSource')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='django_blogconnector.BlogCategory')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='django_blogconnector.BlogUser')),
            ],
        ),
    ]
