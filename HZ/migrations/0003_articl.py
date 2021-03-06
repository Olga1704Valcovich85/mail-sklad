# Generated by Django 4.0.3 on 2022-03-31 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HZ', '0002_alter_own_production_kod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('full', models.TextField(verbose_name='Статья')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HZ.own_production')),
            ],
        ),
    ]
