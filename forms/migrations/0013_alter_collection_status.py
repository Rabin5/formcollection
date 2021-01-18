# Generated by Django 3.1.4 on 2021-01-17 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0012_alter_risk_allowance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formcollection',
            name='status',
            field=models.CharField(choices=[('started', 'STARTED'), ('incomplete', 'INCOMPLETE'), ('submitted', 'SUBMITTED'), ('completed', 'COMPLETED')], default='started', max_length=20),
        ),
        migrations.AlterField(
            model_name='riskallowanceline',
            name='expense_amount',
            field=models.DecimalField(decimal_places=2, max_digits=19, verbose_name='खर्च रकम'),
        ),
    ]
