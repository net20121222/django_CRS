# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=128)),
                ('ssh_username', models.CharField(default=b'', max_length=1024, verbose_name=b'SSH username', blank=True)),
                ('ssh_password', models.CharField(default=b'', max_length=1024, verbose_name=b'SSH password', blank=True)),
                ('ssh_key_data', models.TextField(default=b'', verbose_name=b'SSH privite key', blank=True)),
                ('ssh_key_unlock', models.CharField(default=b'', max_length=1024, verbose_name=b'SSH key unlock', blank=True)),
                ('sudo_username', models.CharField(default=b'', max_length=1024, blank=True)),
                ('sudo_password', models.CharField(default=b'', max_length=1024, blank=True)),
                ('created_by', models.ForeignKey(related_name=b"{u'class': 'credential', u'app_label': 'ansible'}(class)s_created", on_delete=django.db.models.deletion.SET_NULL, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(related_name=b'credentials', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('scmtype', models.CharField(max_length=1024)),
                ('scmurl', models.CharField(max_length=1024, null=True, blank=True)),
                ('group', models.CharField(max_length=128, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name=b"{u'class': 'project', u'app_label': 'ansible'}(class)s_created", on_delete=django.db.models.deletion.SET_NULL, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'permissions': (('access_pro', 'Access Project'), ('config_pro', 'Config Project'), ('execute_pro', 'Execute Project'), ('manager_pro', 'Manager Project')),
            },
            bases=(models.Model,),
        ),
    ]
