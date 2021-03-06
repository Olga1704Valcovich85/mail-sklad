# Generated by Django 4.0.3 on 2022-03-30 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autorization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(max_length=15, null=True)),
                ('otdel', models.CharField(max_length=50, null=True)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='own_production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('articul', models.IntegerField()),
                ('kod', models.IntegerField()),
                ('kolichestvo', models.IntegerField()),
                ('color', models.CharField(max_length=30)),
                ('size', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'мужчина'), ('F', 'женщина')], default='F', max_length=1)),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HZ.user1')),
            ],
        ),
    ]
