# Generated by Django 3.1.4 on 2021-02-18 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0031_merge_20210210_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncompleteConstructionWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master_data.governmentbody', verbose_name='निकायको नाम')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProcurementAuditor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master_data.governmentbody', verbose_name='निकायको नाम')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('fiscal_year', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master_data.fiscalyear', verbose_name='आर्थिक बर्ष')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProcurementAuditorLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('amt_expense_estimate', models.FloatField(verbose_name='लागत अनुमान')),
                ('num_piece', models.FloatField(verbose_name='टुक्रा संख्या')),
                ('amt_expense', models.FloatField(verbose_name='खर्च रकम')),
                ('procurement_auditor_line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lines', to='forms.procurementauditor')),
                ('sub_header', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master_data.subheader', verbose_name='उपशीर्षकको नाम')),
                ('work_nature', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master_data.worknature', verbose_name='कामको प्रकृति')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IncompleteConstructionWorkLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('construction_work', models.CharField(blank=True, max_length=255, null=True, verbose_name='निर्माण कार्य')),
                ('agreement_date', models.DateField(null=True)),
                ('estimated_completion_date', models.DateField(null=True)),
                ('expense', models.FloatField(verbose_name='यो वर्ष सम्मको खर्च')),
                ('progress', models.CharField(blank=True, max_length=255, null=True, verbose_name='भौतिक प्रगति')),
                ('construction_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master_data.constructioncompany', verbose_name='निर्माण व्यवसायी')),
                ('incomplete_construction_work_line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lines', to='forms.incompleteconstructionwork')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]