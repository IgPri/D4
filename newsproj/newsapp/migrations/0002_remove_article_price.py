# Generated by Django 4.0.2 on 2022-06-22 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='price',
        ),
    ]