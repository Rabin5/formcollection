# Generated by Django 3.1.4 on 2021-02-03 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0024_alter_add_related_name_in_relief_procurement_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reliefprocuredistributionline',
            name='reliefprocuredistribution_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='forms.reliefprocuredistribution'),
        ),
    ]