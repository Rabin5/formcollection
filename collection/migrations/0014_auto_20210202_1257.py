# Generated by Django 3.1.4 on 2021-02-02 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0016_merge_20210129_0915'),
        ('collection', '0013_covhosformcollection_approver'),
    ]

    operations = [
        migrations.AddField(
            model_name='chiefministerofficeformcollection',
            name='action_plan_implementation',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.actionplanimplementation'),
        ),
        migrations.AlterField(
            model_name='chiefministerofficeformcollection',
            name='state',
            field=models.IntegerField(blank=True, choices=[(0, 'epidemic_outbreak_prep'), (1, 'fund_receipt_expense'), (2, 'risk_allowance'), (3, 'province_institute_management'), (4, 'action_plan_implementation')], default=0),
        ),
        migrations.AlterField(
            model_name='chiefministerofficeformcollection',
            name='status',
            field=models.CharField(choices=[('started', 'STARTED'), ('incomplete', 'INCOMPLETE'), ('submitted', 'SUBMITTED'), ('completed', 'COMPLETED'), ('approved', 'APPROVED'), ('rejected', 'REJECTED')], default='started', max_length=20),
        ),
        migrations.AlterField(
            model_name='covhosformcollection',
            name='status',
            field=models.CharField(choices=[('started', 'STARTED'), ('incomplete', 'INCOMPLETE'), ('submitted', 'SUBMITTED'), ('completed', 'COMPLETED'), ('approved', 'APPROVED'), ('rejected', 'REJECTED')], default='started', max_length=20),
        ),
        migrations.AlterField(
            model_name='internalaffairformcollection',
            name='status',
            field=models.CharField(choices=[('started', 'STARTED'), ('incomplete', 'INCOMPLETE'), ('submitted', 'SUBMITTED'), ('completed', 'COMPLETED'), ('approved', 'APPROVED'), ('rejected', 'REJECTED')], default='started', max_length=20),
        ),
        migrations.AlterField(
            model_name='locallevelformcollection',
            name='status',
            field=models.CharField(choices=[('started', 'STARTED'), ('incomplete', 'INCOMPLETE'), ('submitted', 'SUBMITTED'), ('completed', 'COMPLETED'), ('approved', 'APPROVED'), ('rejected', 'REJECTED')], default='started', max_length=20),
        ),
        migrations.AlterField(
            model_name='provinceformcollection',
            name='status',
            field=models.CharField(choices=[('started', 'STARTED'), ('incomplete', 'INCOMPLETE'), ('submitted', 'SUBMITTED'), ('completed', 'COMPLETED'), ('approved', 'APPROVED'), ('rejected', 'REJECTED')], default='started', max_length=20),
        ),
    ]