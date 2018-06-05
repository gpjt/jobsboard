# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('filled', models.BooleanField(default=False)),
                ('spam', models.BooleanField(default=False)),
                ('posted_by_user_agent', models.CharField(default=b'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22', max_length=1024)),
                ('posted_from_ip', models.IPAddressField(null=True, blank=True)),
                ('title', models.CharField(max_length=1024)),
                ('job_type', models.CharField(max_length=2, choices=[(b'PT', b'Part-time'), (b'FT', b'Full-time'), (b'FL', b'Freelance'), (b'VL', b'Volunteer'), (b'OT', b'Other')])),
                ('salary', models.CharField(max_length=128, blank=True)),
                ('url', models.CharField(max_length=1024, blank=True)),
                ('location', models.CharField(max_length=1024, blank=True)),
                ('company', models.CharField(max_length=512, blank=True)),
                ('description', models.TextField()),
                ('contact_email', models.EmailField(max_length=254, blank=True)),
                ('experience', models.CharField(max_length=128, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Retweeter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=32)),
                ('access_key', models.CharField(max_length=70)),
                ('access_secret', models.CharField(max_length=70)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
