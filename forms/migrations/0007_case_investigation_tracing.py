# Generated by Django 3.1.4 on 2021-01-25 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0006_add_action_plan_implementation'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseInvestigationTracing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('state', models.CharField(blank=True, choices=[('draft', 'Draft'), ('submitted', 'Submitted')], default='draft', max_length=25)),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master_data.governmentbody', verbose_name='निकायको नामः')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('fiscal_year', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='case_investigation', to='master_data.fiscalyear', verbose_name='आर्थिक बर्ष: ')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='actionplanimplementationline',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master_data.actionplanactivity', verbose_name='क्रियाकलाप'),
        ),
        migrations.AlterField(
            model_name='actionplanimplementationline',
            name='work_done',
            field=models.CharField(max_length=500, verbose_name='प्रदेश सरकारबाट भएको कार्य'),
        ),
        migrations.AlterField(
            model_name='actionplanimplementationline',
            name='work_expense',
            field=models.FloatField(verbose_name='उक्त कार्यमा भएको खर्च'),
        ),
        migrations.AlterField(
            model_name='formcollection',
            name='state',
            field=models.IntegerField(blank=True, choices=[(0, 'fund_receipt_expense'), (1, 'risk_allowance'), (2, 'medical_expense'), (3, 'medical_receipt'), (4, 'medical_use'), (5, 'med_purchase_desc'), (6, 'pcr_test_compliance_detail'), (7, 'pcr_lab_detail'), (8, 'rdt_test_detail'), (9, 'pcr_kit_usage'), (10, 'epidemic_outbreak_preparatory'), (11, 'action_plan_implementation')], default=1),
        ),
        migrations.CreateModel(
            name='CaseInvestigationTracingLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('description', models.TextField(verbose_name='वर्णन')),
                ('num_team_members', models.PositiveIntegerField(verbose_name='टोली सदस्यहरूको संख्या')),
                ('amount_expense', models.FloatField(verbose_name='खर्च रकम')),
                ('num_searched_cases', models.IntegerField(verbose_name='खोजी गरिएका केसहरूको संख्या')),
                ('num_identified_infection', models.IntegerField(verbose_name='पहिचान भएका घटनाहरूको संख्या')),
                ('remarks', models.CharField(max_length=200, verbose_name='कैफियत')),
                ('case_investigation_tracing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms.caseinvestigationtracing', verbose_name='केस अनुसन्धान ट्रेसिंग')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
