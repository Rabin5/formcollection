# Generated by Django 3.1.4 on 2021-01-27 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('forms', '0002_auto_20210127_1133'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FormCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(blank=True, choices=[(0, 'fund_receipt_expense'), (1, 'risk_allowance'), (2, 'medical_expense'), (3, 'medical_receipt'), (4, 'medical_use'), (5, 'med_purchase_desc'), (6, 'pcr_test_compliance_detail'), (7, 'pcr_lab_detail'), (8, 'rdt_test_detail'), (9, 'pcr_kit_usage'), (10, 'covid_hos_mainpower'), (11, 'cov_hos_equipment'), (12, 'covid_hospital_detail'), (13, 'quarantine_management_detail'), (14, 'isolation_management_detail'), (15, 'quarantine_contruction_expenditure'), (16, 'isolation_construction_expenditure'), (17, 'cov_hos_management_checklist')], default=0)),
                ('status', models.CharField(choices=[('started', 'STARTED'), ('incomplete', 'INCOMPLETE'), ('submitted', 'SUBMITTED'), ('completed', 'COMPLETED')], default='started', max_length=20)),
                ('cov_hos_equipment', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.covidhospitalequipment')),
                ('cov_hos_management_checklist', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.covidhospitalmanagementchecklist')),
                ('covid_hos_mainpower', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.covidhospitalmanpower')),
                ('covid_hospital_detail', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.covidhospitaldetail')),
                ('fund_receipt_expense', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.fundreceiptexpense')),
                ('isolation_construction_expenditure', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.isolationconstructionexependiture')),
                ('isolation_management_detail', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.isolationmanagementdetail')),
                ('med_purchase_desc', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.medicalpurchasedescription')),
                ('medical_expense', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.medicalexpense')),
                ('medical_receipt', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.medicalreceipt')),
                ('medical_use', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.medicaluse')),
                ('pcr_kit_usage', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.pcrkitusage')),
                ('pcr_lab_detail', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.pcrlaboratorydetail')),
                ('pcr_test_compliance_detail', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.pcrtestcompliancedetail')),
                ('quarantine_contruction_expenditure', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.quarantineconstructionexpenditure')),
                ('quarantine_management_detail', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.quarantinemanagementdetail')),
                ('rdt_test_detail', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.rdttestdetail')),
                ('risk_allowance', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.riskallowance')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]