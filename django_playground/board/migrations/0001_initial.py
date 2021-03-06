# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-15 06:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_summernote.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_summernote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummerNote',
            fields=[
                ('attachment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_summernote.Attachment')),
                ('summer_field', django_summernote.fields.SummernoteTextField(default='')),
            ],
            options={
                'abstract': False,
            },
            bases=('django_summernote.attachment',),
        ),
    ]
