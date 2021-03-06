# Generated by Django 3.1.4 on 2021-03-14 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='नाम')),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='नाम')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='नाम')),
            ],
        ),
    ]
