# Generated by Django 3.1.4 on 2021-02-03 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0023_alter_add_related_name_in_case_investigation_tracing_operation_line'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reliefprocurementdetailline',
            name='reliefprocurementdetail_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='forms.reliefprocurementdetail'),
        ),
    ]
