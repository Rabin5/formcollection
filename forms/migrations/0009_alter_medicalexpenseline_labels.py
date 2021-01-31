# Generated by Django 3.1.4 on 2021-01-28 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
        ('forms', '0008_alter_medicalexpenseline_add_importer_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalexpenseline',
            name='importer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expenses', to='master_data.importer', verbose_name='आपूर्तिकर्ताको नाम'),
        ),
        migrations.AlterField(
            model_name='medicalexpenseline',
            name='procure_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expenses', to='master_data.procurementmethod', verbose_name='खरिद विधि'),
        ),
        migrations.AlterField(
            model_name='medicalexpenseline',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='master_data.product', verbose_name='स्वास्थ्य सामाग्री उपकरण'),
        ),
        migrations.AlterField(
            model_name='medicalreceiptline',
            name='provider_body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='body_pro', to='master_data.governmentbody', verbose_name='यदि निकाय भए, प्रदान गर्ने निकाय'),
        ),
        migrations.AlterField(
            model_name='medicalreceiptline',
            name='provider_institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='institution_pro', to='master_data.institution', verbose_name='यदि संस्था भए, प्रदान गर्ने संस्था'),
        ),
    ]