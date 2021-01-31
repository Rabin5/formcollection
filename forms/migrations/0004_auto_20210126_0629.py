# Generated by Django 3.1.4 on 2021-01-26 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_district_covid_management'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='districtcovidmanagement',
            name='body',
        ),
        migrations.RemoveField(
            model_name='districtcovidmanagement',
            name='create_user',
        ),
        migrations.RemoveField(
            model_name='districtcovidmanagement',
            name='fiscal_year',
        ),
        migrations.RemoveField(
            model_name='districtisolationmanagementline',
            name='district',
        ),
        migrations.RemoveField(
            model_name='districtisolationmanagementline',
            name='isolation_mgmt_lines',
        ),
        migrations.RemoveField(
            model_name='districtlabtestline',
            name='district',
        ),
        migrations.RemoveField(
            model_name='districtlabtestline',
            name='lab_test_lines',
        ),
        migrations.DeleteModel(
            name='DisctrictQuarantineManagementLine',
        ),
        migrations.DeleteModel(
            name='DistrictCovidManagement',
        ),
        migrations.DeleteModel(
            name='DistrictIsolationManagementLine',
        ),
        migrations.DeleteModel(
            name='DistrictLabTestLine',
        ),
    ]