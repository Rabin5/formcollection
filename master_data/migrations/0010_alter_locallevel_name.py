# Generated by Django 3.1.4 on 2021-02-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0009_alter_master_data_fieldlengths'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locallevel',
            name='name',
            field=models.CharField(max_length=300, verbose_name='स्थानीय स्तर'),
        ),
    ]