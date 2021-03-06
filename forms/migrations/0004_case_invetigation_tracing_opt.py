# Generated by Django 3.1.4 on 2021-01-28 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0003_merge_20210128_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseInvestigationTracingOperations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='case_inves_tracing_operation_body', to='master_data.governmentbody', verbose_name='निकायको नामः: ')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('fiscal_year', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='_tracing_operation_fiscal_year', to='master_data.fiscalyear', verbose_name='आर्थिक बर्ष: ')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='covidhospitalequipment',
            name='cov_hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forms_cov_hos', to='master_data.covidhospital', verbose_name='कोभिड डेडिकेटेड अस्पातालको नाम:'),
        ),
        migrations.AlterField(
            model_name='medicalexpenseline',
            name='amt_agreement',
            field=models.DecimalField(decimal_places=2, max_digits=19, verbose_name='सम्झौता रकम '),
        ),
        migrations.AlterField(
            model_name='medicalexpenseline',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='master_data.product', verbose_name='स्वास्थ्य सामाग्री उपकरणको विवरण'),
        ),
        migrations.AlterField(
            model_name='medicaluseline',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master_data.product', verbose_name='औषधी स्वास्थ्य सामग्री एवं उपकरणको नाम'),
        ),
        migrations.AlterField(
            model_name='pcrlaboratorydetailline',
            name='time_test_result',
            field=models.FloatField(blank=True, null=True, verbose_name='नतिजा दिन लाग्ने औषत समय'),
        ),
        migrations.CreateModel(
            name='CaseInvestigationTracingOperationsLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('num_team_members', models.IntegerField(blank=True, null=True, verbose_name='टीमको सदस्य संख्या')),
                ('amt_expense', models.FloatField(blank=True, null=True, verbose_name='खर्च रकम')),
                ('num_case', models.IntegerField(blank=True, null=True, verbose_name='केश अनुसन्धान संख्या')),
                ('num_contact_identified', models.IntegerField(blank=True, null=True, verbose_name='कन्टयाक्टमाआएकाव्यक्तिहरूकोपहीचान संख्या')),
                ('num_consult_refer', models.IntegerField(blank=True, null=True, verbose_name='सामान्य परामर्श, फलोअप तथा रेफर संख्या')),
                ('num_sample_collect_test', models.IntegerField(blank=True, null=True, verbose_name='नमूना संकलन वा द्रुत परिक्षण संख्या')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_investigation_body', to='master_data.governmentbody', verbose_name='निकायको नामः: ')),
                ('caseinvestigationtracingoperations_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.caseinvestigationtracingoperations')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
