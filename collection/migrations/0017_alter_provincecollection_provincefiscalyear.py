# Generated by Django 3.1.4 on 2021-02-05 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
        ('collection', '0016_alter_covidhospitalcollection_fiscalyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='provinceformcollection',
            name='body',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='master_data.governmentbody'),
        ),
        migrations.AddField(
            model_name='provinceformcollection',
            name='fiscal_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='master_data.fiscalyear'),
        ),
        migrations.AddField(
            model_name='provinceformcollection',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='master_data.province'),
        ),
    ]
