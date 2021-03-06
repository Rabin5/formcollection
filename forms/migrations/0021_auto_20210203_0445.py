# Generated by Django 3.1.4 on 2021-02-03 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
        ('forms', '0020_merge_20210202_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionplanimplementationline',
            name='action_plan_implementation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lines', to='forms.actionplanimplementation', verbose_name='कार्य योजना कार्यान्वयन'),
        ),
        migrations.AlterField(
            model_name='medicalexpenseline',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='master_data.product', verbose_name='स्वास्थ्य सामाग्री उपकरण'),
        ),
        migrations.AlterField(
            model_name='medicaluseline',
            name='medical_use_line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lines', to='forms.medicaluse'),
        ),
    ]
