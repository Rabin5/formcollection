# Generated by Django 3.1.4 on 2021-01-28 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0004_case_invetigation_tracing_opt'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReliefProcureDistribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reliefprocuredistribution_body', to='master_data.governmentbody', verbose_name='निकायको नामः: ')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('fiscal_year', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reliefprocuredistribution_fiscal_year', to='master_data.fiscalyear', verbose_name='आर्थिक बर्ष: ')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReliefProcureDistributionLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('qty_purchase', models.FloatField(blank=True, null=True, verbose_name='खरिद परिमाण ')),
                ('rate', models.FloatField(blank=True, null=True, verbose_name='प्रतिईकाइ दर')),
                ('amt_total', models.FloatField(blank=True, null=True, verbose_name='रकम')),
                ('qty_distributed', models.FloatField(blank=True, null=True, verbose_name='वितरण परिमाण')),
                ('qty_remaining', models.FloatField(blank=True, null=True, verbose_name='बाँकी परिमाण ')),
                ('has_quality_complaint', models.BooleanField(verbose_name='गुणस्तरमा सिकायत छ । छैन')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_investigation_body', to='master_data.product', verbose_name='राहत सामग्री')),
                ('reliefprocuredistribution_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.reliefprocuredistribution')),
                ('uom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_data.unitofmeasure', verbose_name='ईकाइ')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
