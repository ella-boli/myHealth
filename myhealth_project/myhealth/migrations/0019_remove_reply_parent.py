# Generated by Django 2.2.2 on 2020-08-14 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhealth', '0018_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='parent',
        ),
    ]