# Generated by Django 4.0.3 on 2022-03-31 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HZ', '0004_alter_articl_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articl',
            name='user_name',
        ),
    ]