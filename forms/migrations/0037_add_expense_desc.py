# Generated by Django 3.1.4 on 2021-02-22 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0036_add_recover_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseDesc',
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
            name='ExpenseDescLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('gross_internal_income', models.FloatField(verbose_name='कूल आन्तरिक आय')),
                ('official_expsense', models.FloatField(verbose_name='प्रशासनिक खर्च')),
                ('financial_support_expense', models.FloatField(verbose_name='आथिंक सहायता खर्च')),
                ('future_expense', models.FloatField(verbose_name='भैपरी आउने खर्च')),
                ('capital_expenditure', models.FloatField(verbose_name='पूजीगत खर्च')),
                ('expense_desc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lines', to='forms.expensedesc')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
