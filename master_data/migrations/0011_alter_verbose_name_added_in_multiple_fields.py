# Generated by Django 3.1.4 on 2021-02-17 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0010_alter_locallevel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionplanactivity',
            name='description',
            field=models.TextField(verbose_name='वर्णन'),
        ),
        migrations.AlterField(
            model_name='actionplanactivity',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='शीर्षक'),
        ),
        migrations.AlterField(
            model_name='allowancetype',
            name='description',
            field=models.TextField(verbose_name='वर्णन'),
        ),
        migrations.AlterField(
            model_name='allowancetype',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='नाम'),
        ),
        migrations.AlterField(
            model_name='committee',
            name='description',
            field=models.TextField(verbose_name='वर्णन'),
        ),
        migrations.AlterField(
            model_name='committee',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='नाम'),
        ),
        migrations.AlterField(
            model_name='covidhospital',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.country', verbose_name='देश'),
        ),
        migrations.AlterField(
            model_name='covidhospital',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.district', verbose_name='जिल्ला'),
        ),
        migrations.AlterField(
            model_name='covidhospital',
            name='local_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.locallevel', verbose_name='स्थानीय निकाय'),
        ),
        migrations.AlterField(
            model_name='covidhospital',
            name='ward',
            field=models.IntegerField(blank=True, null=True, verbose_name='वार्ड न'),
        ),
        migrations.AlterField(
            model_name='covidhospitalmanagementchecklistdescription',
            name='description',
            field=models.TextField(verbose_name='वर्णन'),
        ),
        migrations.AlterField(
            model_name='expenseheader',
            name='description',
            field=models.TextField(verbose_name='वर्णन'),
        ),
        migrations.AlterField(
            model_name='expenseheader',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='शीर्षक'),
        ),
        migrations.AlterField(
            model_name='governmentbody',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.country', verbose_name='देश'),
        ),
        migrations.AlterField(
            model_name='governmentbody',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.district', verbose_name='जिल्ला'),
        ),
        migrations.AlterField(
            model_name='governmentbody',
            name='local_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.locallevel', verbose_name='स्थानीय निकाय'),
        ),
        migrations.AlterField(
            model_name='governmentbody',
            name='ward',
            field=models.IntegerField(blank=True, null=True, verbose_name='वार्ड न'),
        ),
        migrations.AlterField(
            model_name='importer',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.country', verbose_name='देश'),
        ),
        migrations.AlterField(
            model_name='importer',
            name='date_establishment',
            field=models.DateField(null=True, verbose_name='स्थापना मिति'),
        ),
        migrations.AlterField(
            model_name='importer',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.district', verbose_name='जिल्ला'),
        ),
        migrations.AlterField(
            model_name='importer',
            name='local_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.locallevel', verbose_name='स्थानीय निकाय'),
        ),
        migrations.AlterField(
            model_name='importer',
            name='name',
            field=models.CharField(max_length=300, verbose_name='नाम'),
        ),
        migrations.AlterField(
            model_name='importer',
            name='ward',
            field=models.IntegerField(blank=True, null=True, verbose_name='वार्ड न'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.country', verbose_name='देश'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='date_establishment',
            field=models.DateField(null=True, verbose_name='स्थापना मिति'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.district', verbose_name='जिल्ला'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='local_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.locallevel', verbose_name='स्थानीय निकाय'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(max_length=300, verbose_name='नाम'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='ward',
            field=models.IntegerField(blank=True, null=True, verbose_name='वार्ड न'),
        ),
        migrations.AlterField(
            model_name='isolationcenter',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.country', verbose_name='देश'),
        ),
        migrations.AlterField(
            model_name='isolationcenter',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.district', verbose_name='जिल्ला'),
        ),
        migrations.AlterField(
            model_name='isolationcenter',
            name='local_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.locallevel', verbose_name='स्थानीय निकाय'),
        ),
        migrations.AlterField(
            model_name='isolationcenter',
            name='name',
            field=models.CharField(max_length=300, verbose_name='नाम'),
        ),
        migrations.AlterField(
            model_name='isolationcenter',
            name='ward',
            field=models.IntegerField(blank=True, null=True, verbose_name='वार्ड न'),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='capacity_daily_test',
            field=models.IntegerField(default=0, verbose_name='दैनिक परीक्षण क्षमता'),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.country', verbose_name='देश'),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='date_establishment',
            field=models.DateField(null=True, verbose_name='स्थापना मिति'),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.district', verbose_name='जिल्ला'),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='local_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.locallevel', verbose_name='स्थानीय निकाय'),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='name',
            field=models.CharField(max_length=300, verbose_name='नाम'),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='ward',
            field=models.IntegerField(blank=True, null=True, verbose_name='वार्ड न'),
        ),
        migrations.AlterField(
            model_name='officebearer',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='शीर्षक'),
        ),
        migrations.AlterField(
            model_name='quanrantinecenter',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.country', verbose_name='देश'),
        ),
        migrations.AlterField(
            model_name='quanrantinecenter',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.district', verbose_name='जिल्ला'),
        ),
        migrations.AlterField(
            model_name='quanrantinecenter',
            name='local_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.locallevel', verbose_name='स्थानीय निकाय'),
        ),
        migrations.AlterField(
            model_name='quanrantinecenter',
            name='name',
            field=models.CharField(max_length=300, verbose_name='नाम'),
        ),
        migrations.AlterField(
            model_name='quanrantinecenter',
            name='ward',
            field=models.IntegerField(blank=True, null=True, verbose_name='वार्ड न'),
        ),
        migrations.AlterField(
            model_name='relieftype',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='शीर्षक'),
        ),
        migrations.AlterField(
            model_name='sourcebudget',
            name='description',
            field=models.TextField(verbose_name='वर्णन'),
        ),
        migrations.AlterField(
            model_name='sourcebudget',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True, verbose_name='शीर्षक'),
        ),
    ]
