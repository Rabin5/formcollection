# Generated by Django 3.1.4 on 2021-02-25 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0033_dprexpense_dprexpenseline_quarterlyprogram_quarterlyprogramline_yearlytarget_yearlytargetline'),
    ]

    operations = [
        migrations.CreateModel(
            name='RevenueDistribution',
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
            name='RevenueDistributionLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('title', models.CharField(blank=True, max_length=300, null=True, verbose_name='आय शीर्षक')),
                ('collected_amount', models.FloatField(verbose_name='संकलित रकम')),
                ('percentage_sent_state', models.FloatField(verbose_name='प्रदेशलाई पठाउनु पर्ने प्रतिशत')),
                ('sent_amount', models.FloatField(verbose_name='पठाएको रकम')),
                ('remaining_amount', models.TextField(blank=True, null=True, verbose_name='पठाउन बाँकी रकम')),
                ('revenue_distribution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lines', to='forms.revenuedistribution')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]