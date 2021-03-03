# Generated by Django 3.1.4 on 2021-02-19 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master_data', '0001_initial'),
        ('forms', '0032_incompleteconstructionwork_incompleteconstructionworkline_procurementauditor_procurementauditorline'),
    ]

    operations = [
        migrations.CreateModel(
            name='DPRExpense',
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
        migrations.CreateModel(
            name='QuarterlyProgram',
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
        migrations.CreateModel(
            name='YearlyTarget',
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
        migrations.CreateModel(
            name='YearlyTargetLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('plan', models.CharField(blank=True, max_length=255, null=True, verbose_name='कार्यक्रम / योजना')),
                ('amt_expense', models.FloatField(verbose_name='यो वर्ष खर्च')),
                ('financial_progress', models.FloatField(verbose_name='वित्तिय प्रगति')),
                ('physical_progress', models.FloatField(verbose_name='भौतिक प्रगति')),
                ('description', models.TextField(blank=True, null=True, verbose_name='७५% भन्दा न्युन प्रगति भएकोमा सो को कारण')),
                ('yearly_target_line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lines', to='forms.yearlytarget')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuarterlyProgramLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('budget_subtiles', models.FloatField(verbose_name='बजेट उपशीर्षक')),
                ('total_expense', models.FloatField(verbose_name='कुल खर्च')),
                ('first_quarter_expense', models.FloatField(verbose_name='प्रथम चौमासिक खर्च')),
                ('second_quarter_expense', models.FloatField(verbose_name='दोस्रो चौमासिक खर्च')),
                ('third_quarter_expense', models.FloatField(verbose_name='तेस्रो चौमासिक खर्च')),
                ('fiscal_month_expense', models.FloatField(verbose_name='आषाढ महिना चौमासिक खर्च')),
                ('quarterly_program_line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lines', to='forms.quarterlyprogram')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DPRExpenseLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('program_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='कार्यक्रमको नाम')),
                ('approved_budget', models.FloatField(verbose_name='स्वीकृत बजेट')),
                ('amt_expense', models.FloatField(verbose_name='खर्च रकम')),
                ('determined_budget', models.FloatField(verbose_name='अध्ययनबाट निर्धारण भएका आयोजनाको लागत')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_data.consultant', verbose_name='परामर्शदाता')),
                ('drp_expense_line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lines', to='forms.dprexpense')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
