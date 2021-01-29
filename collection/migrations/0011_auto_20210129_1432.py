# Generated by Django 3.1.4 on 2021-01-29 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0010_auto_20210129_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locallevelformcollection',
            name='state',
            field=models.IntegerField(blank=True, choices=[(0, 'epidemic_outbreak_prep'), (1, 'fund_receipt_expense'), (2, 'risk_allowance'), (3, 'medical_expense'), (4, 'medical_receipt'), (5, 'medical_use'), (6, 'med_purchase_desc'), (7, 'case_investigation_tracing'), (8, 'covid_hos_mainpower'), (9, 'cov_hos_equipment'), (10, 'quarantine_management_detail'), (11, 'isolation_management_detail'), (12, 'quarantine_contruction_expenditure'), (13, 'isolation_construction_expenditure'), (14, 'case_investigation_tracing_operation'), (15, 'relief_procurement_detail'), (16, 'relief_procurement_distribution'), (17, 'ward_relief_procurement_dist'), (18, 'received_relief_detail'), (19, 'relief_distribution_expense'), (20, 'action_plan_implementation')], default=0),
        ),
    ]
