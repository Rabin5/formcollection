# Generated by Django 3.1.4 on 2021-01-29 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0009_auto_20210129_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locallevelformcollection',
            old_name='cov_hos_manpower',
            new_name='covid_hos_mainpower',
        ),
    ]
