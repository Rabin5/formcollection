# Generated by Django 3.1.4 on 2021-01-27 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0002_auto_20210127_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('state', models.CharField(blank=True, choices=[('draft', 'Draft'), ('submitted', 'Submitted')], default='draft', max_length=25)),
                ('body', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='fund_operation', to='master_data.governmentbody', verbose_name='निकायको नामः: ')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('fiscal_year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='fund_operation', to='master_data.fiscalyear', verbose_name='आर्थिक बर्ष: ')),
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
            name='FundOperationLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('amt_received', models.FloatField(verbose_name='प्राप्त रकम')),
                ('amt_expensed', models.FloatField(verbose_name='खर्च रकम')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fund_operation_line', to='master_data.governmentbody', verbose_name='उपलब्ध गराउने निकाय:')),
                ('expense_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fund_operation_line', to='master_data.expenseheader', verbose_name='खर्चको शीर्षक')),
                ('fund_operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='forms.fundoperation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
