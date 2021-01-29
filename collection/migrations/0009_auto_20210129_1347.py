# Generated by Django 3.1.4 on 2021-01-29 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0013_auto_20210129_1347'),
        ('collection', '0008_merge_20210129_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provinceformcollection',
            name='state',
            field=models.IntegerField(blank=True, choices=[(0, 'epidemic_outbreak_prep'), (1, 'fund_receipt_expense'), (2, 'risk_allowance'), (3, 'medical_expense'), (4, 'medical_receipt'), (5, 'medical_use'), (6, 'med_purchase_desc'), (7, 'pcr_test_compliance_detail'), (8, 'pcr_lab_detail'), (9, 'rdt_test_detail'), (10, 'pcr_kit_usage'), (11, 'covid_hos_mainpower'), (12, 'cov_hos_equipment'), (13, 'covid_hospital_detail'), (14, 'quarantine_management_detail'), (15, 'isolation_management_detail'), (16, 'quarantine_contruction_expenditure'), (17, 'isolation_construction_expenditure'), (18, 'district_covid_management'), (19, 'fund_operation')], default=0),
        ),
        migrations.CreateModel(
            name='LocalLevelFormCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(blank=True, choices=[(0, 'epidemic_outbreak_prep'), (1, 'fund_receipt_expense'), (2, 'risk_allowance'), (3, 'medical_expense'), (4, 'medical_receipt'), (5, 'medical_use'), (6, 'med_purchase_desc'), (7, 'pcr_test_compliance_detail'), (8, 'pcr_lab_detail'), (9, 'rdt_test_detail'), (10, 'pcr_kit_usage'), (11, 'covid_hos_mainpower'), (12, 'cov_hos_equipment'), (13, 'covid_hospital_detail'), (14, 'quarantine_management_detail'), (15, 'isolation_management_detail'), (16, 'quarantine_contruction_expenditure'), (17, 'isolation_construction_expenditure'), (18, 'district_covid_management'), (19, 'fund_operation')], default=0)),
                ('status', models.CharField(choices=[('started', 'STARTED'), ('incomplete', 'INCOMPLETE'), ('submitted', 'SUBMITTED'), ('completed', 'COMPLETED')], default='started', max_length=20)),
                ('action_plan_implementation', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.actionplanimplementation')),
                ('case_investigation_tracing', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.caseinvestigationtracing')),
                ('case_investigation_tracing_operation', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.caseinvestigationtracingoperations')),
                ('cov_hos_equipment', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.covidhospitalequipment')),
                ('cov_hos_manpower', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.covidhospitalmanpower')),
                ('epidemic_outbreak_prep', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.epidemicoutbreakpreparatorywork')),
                ('fund_receipt_expense', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.fundreceiptexpense')),
                ('isolation_construction_expenditure', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.isolationconstructionexependiture')),
                ('isolation_management_detail', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.isolationmanagementdetail')),
                ('med_purchase_desc', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.medicalpurchasedescription')),
                ('medical_expense', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.medicalexpense')),
                ('medical_receipt', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.medicalreceipt')),
                ('medical_use', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.medicaluse')),
                ('quarantine_contruction_expenditure', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.quarantineconstructionexpenditure')),
                ('quarantine_management_detail', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.quarantinemanagementdetail')),
                ('received_relief_detail', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.receivedreliefdetail')),
                ('relief_distribution_expense', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.reliefdistributionexpense')),
                ('relief_procurement_detail', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.reliefprocurementdetail')),
                ('relief_procurement_distribution', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.reliefprocuredistribution')),
                ('risk_allowance', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.riskallowance')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ward_relief_procurement_dist', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.wardreliefprocuredistribution')),
            ],
        ),
    ]
