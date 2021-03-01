# Generated by Django 3.1.4 on 2021-02-21 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0011_add_contract_desc'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0034_add_designation_vacancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='designationvacancyline',
            name='designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='designation_vacancy_lines', to='master_data.designation', verbose_name='स्वीकृत पद'),
        ),
        migrations.CreateModel(
            name='ContractDescLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='ठेक्काको विवरण')),
                ('agreement_date', models.DateField(verbose_name='सम्झौता मिति')),
                ('contract_duration', models.PositiveIntegerField(verbose_name='ठेक्का अवधि')),
                ('contract_amount', models.FloatField(verbose_name='ठेक्का रकम')),
                ('recover_amount', models.FloatField(verbose_name='असुली रकम')),
                ('remaining_recover_amount', models.FloatField(verbose_name='असुल हुन बाँकी')),
                ('remarks', models.CharField(blank=True, max_length=500, null=True, verbose_name='कैफियत')),
                ('contract_desc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lines', to='forms.contractdesc')),
                ('contractor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractor_desc_lines', to='master_data.contractor', verbose_name='ठेकेदारको नाम')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
