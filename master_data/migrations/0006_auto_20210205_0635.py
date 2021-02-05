# Generated by Django 3.1.4 on 2021-02-05 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0005_alter_covidhospitalcollection_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=300, verbose_name='देश'),
        ),
        migrations.AlterField(
            model_name='covidhospital',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.province', verbose_name='प्रदेश'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=300, verbose_name='जिल्ला'),
        ),
        migrations.AlterField(
            model_name='district',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='province_to_district', to='master_data.province', verbose_name='प्रदेश'),
        ),
        migrations.AlterField(
            model_name='governmentbody',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.province', verbose_name='प्रदेश'),
        ),
        migrations.AlterField(
            model_name='importer',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.province', verbose_name='प्रदेश'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.province', verbose_name='प्रदेश'),
        ),
        migrations.AlterField(
            model_name='isolationcenter',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.province', verbose_name='प्रदेश'),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.province', verbose_name='प्रदेश'),
        ),
        migrations.AlterField(
            model_name='locallevel',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='local_to_district', to='master_data.district', verbose_name='जिल्ला'),
        ),
        migrations.AlterField(
            model_name='locallevel',
            name='name',
            field=models.CharField(max_length=300, verbose_name='स्थानीय स्तर'),
        ),
        migrations.AlterField(
            model_name='province',
            name='name',
            field=models.CharField(max_length=300, verbose_name='प्रदेश'),
        ),
        migrations.AlterField(
            model_name='quanrantinecenter',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.province', verbose_name='प्रदेश'),
        ),
    ]