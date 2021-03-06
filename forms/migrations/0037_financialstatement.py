# Generated by Django 3.1.4 on 2021-02-25 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0036_consumercommitteecons_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialStatement',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(
                    auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(
                    auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('create_user', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RevenueDistributedLine',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(
                    auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(
                    auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('desc', models.CharField(max_length=300, verbose_name='विवरण')),
                ('is_true', models.BooleanField(
                    default=False, verbose_name='छ वा छैन')),
                ('remaining_distribution', models.FloatField(
                    verbose_name='बाँडफाँड गर्न बाँकी रकम')),
                ('remaining_amount_federal_gov', models.FloatField(
                    verbose_name='संघीय सरकारलाई पठाउन बाँकी रकम')),
                ('remaining_amount_state_gov', models.FloatField(
                    verbose_name='प्रदेश सरकारलाई पठाउन बाँकी रकम')),
                ('way_of_looking', models.CharField(
                    max_length=300, verbose_name='हेर्ने तरिका')),
                ('financialstatement_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                              related_name='lines_renenu', to='forms.financialstatement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RemainingAdvanceLine',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(
                    auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(
                    auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('remaining_advance', models.CharField(
                    max_length=300, verbose_name='५ पेश्की बाँकी ')),
                ('not_expired', models.CharField(
                    max_length=300, verbose_name='म्याद ननाघेको')),
                ('expired', models.CharField(
                    max_length=300, verbose_name='म्याद नाघेको')),
                ('total', models.FloatField(verbose_name='जम्मा')),
                ('way_of_looking', models.CharField(
                    max_length=300, verbose_name='हेर्ने तरिका')),
                ('financialstatement_line', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='lines_ad', to='forms.financialstatement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GrantReturnLine',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(
                    auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(
                    auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('desc', models.CharField(max_length=300, verbose_name='विवरण')),
                ('is_true', models.BooleanField(
                    default=False, verbose_name='छ वा छैन')),
                ('remaining_per_federal_government', models.FloatField(
                    verbose_name='संघीय सरकारतर्फको बाँकी')),
                ('remaining_per_state_government', models.FloatField(
                    verbose_name='प्रदेश सरकारतर्फको बाँकी')),
                ('remaining', models.FloatField(
                    verbose_name='जम्मा फिर्ता गर्न बाँकी')),
                ('way_of_looking', models.CharField(
                    max_length=300, verbose_name='हेर्ने तरिका')),
                ('financialstatement_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                              related_name='lines_grant', to='forms.financialstatement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FinancialStatementResponsibilityLine',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(
                    auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(
                    auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('desc', models.CharField(max_length=300, verbose_name='विवरण')),
                ('is_true', models.BooleanField(
                    default=False, verbose_name='छ वा छैन')),
                ('deadline', models.DateField(
                    verbose_name='गतको बर्षको अन्तिम मौदात')),
                ('start_date', models.DateField(
                    verbose_name='यस बर्षको सुरु मौदात')),
                ('increased_responsibility', models.CharField(
                    max_length=300, verbose_name='निर्माण कार्यमा भएको कुल खर्च')),
                ('num_insufficient_bed', models.IntegerField(
                    verbose_name='घटि वढि जिम्मेवारी')),
                ('way_of_looking', models.CharField(
                    max_length=300, verbose_name='हेर्ने तरिका')),
                ('financialstatement_line', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='forms.financialstatement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FinancialStatementDeductAmountLine',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(
                    auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(
                    auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('desc', models.CharField(max_length=300, verbose_name='विवरण')),
                ('amount', models.FloatField(verbose_name='रकम')),
                ('way_of_looking', models.CharField(
                    max_length=300, verbose_name='हेर्ने तरिका')),
                ('financialstatement_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                              related_name='lines_finalst', to='forms.financialstatement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FinancialStatementBankAccountReconciledLine',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(
                    auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(
                    auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('desc', models.CharField(max_length=300, verbose_name='विवरण')),
                ('is_true', models.BooleanField(
                    default=False, verbose_name='छ वा छैन')),
                ('remaining_per_account', models.FloatField(
                    verbose_name='खाता अनुसारको बाँकी')),
                ('remaining_per_bank', models.FloatField(
                    verbose_name='बैंक अनुसार बाँकी')),
                ('difference', models.FloatField(verbose_name='फरक')),
                ('way_of_looking', models.CharField(
                    max_length=300, verbose_name='हेर्ने तरिका')),
                ('financialstatement_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                              related_name='lines_bankac', to='forms.financialstatement')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
