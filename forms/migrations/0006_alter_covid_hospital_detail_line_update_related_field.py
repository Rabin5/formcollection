# Generated by Django 3.1.4 on 2021-01-29 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_alter_add_realted_lines_in_fk_field_of_lines_of_covid_hospital_manpower_isolatn_constructn_exp_isolatn_mgmt_detail_pcr_test_comp_rdt_test_det'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covidhospitaldetailline',
            name='covidhospital_hospital_detail_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lines', to='forms.covidhospitaldetail'),
        ),
    ]
