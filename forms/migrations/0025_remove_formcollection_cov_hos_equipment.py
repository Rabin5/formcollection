# Generated by Django 3.1.4 on 2021-01-18 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0024_auto_20210118_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formcollection',
            name='cov_hos_equipment',
        ),
    ]
