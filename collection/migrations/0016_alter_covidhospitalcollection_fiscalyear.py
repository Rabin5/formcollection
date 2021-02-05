# Generated by Django 3.1.4 on 2021-02-03 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0005_alter_covidhospitalcollection_body'),
        ('collection', '0015_alter_covidhospitalcollection_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='covhosformcollection',
            name='fiscal_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='master_data.fiscalyear'),
        ),
    ]