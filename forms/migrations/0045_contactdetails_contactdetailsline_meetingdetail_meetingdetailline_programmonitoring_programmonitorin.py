# Generated by Django 3.1.4 on 2021-03-15 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master_data', '0002_employertype_industry_trainingcenter'),
        ('forms', '0044_adminoperativeexpense_adminoperativeexpenseline'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MeetingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProgramMonitoring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProgramMonitoringLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('program_name', models.CharField(max_length=255, verbose_name='आयोजनाको नाम')),
                ('follow_up_date', models.DateField(verbose_name='अनुगमन मित')),
                ('behaviour', models.TextField(verbose_name='बैठकको निर्णयहरु')),
                ('fiscal_year', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master_data.fiscalyear', verbose_name='आर्थिक बर्ष')),
                ('monitoring_body', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master_data.governmentbody', verbose_name='अनुगमन गर्ने निकाय/ संयन्त्र')),
                ('program_monitoring_line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lines', to='forms.programmonitoring')),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MeetingDetailLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('meeting_date', models.DateField(verbose_name='बैठक बसेको मितिहरू')),
                ('meeting_conclusion', models.TextField(verbose_name='बैठकको निर्णयहरु')),
                ('fiscal_year', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master_data.fiscalyear', verbose_name='आर्थिक बर्ष')),
                ('meeting_detail_line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lines', to='forms.meetingdetail')),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactDetailsLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('designation', models.CharField(max_length=255, verbose_name='पद')),
                ('name', models.CharField(max_length=255, verbose_name='नाम')),
                ('contact_number', models.IntegerField(verbose_name='सम्पर्क नम्बर')),
                ('email', models.CharField(max_length=255, verbose_name='सम्पर्क इमेल ')),
                ('contact_details_line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lines', to='forms.contactdetails')),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
        ),
    ]
