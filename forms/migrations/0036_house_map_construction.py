# Generated by Django 3.1.4 on 2021-02-22 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master_data', '0021_house_map_construction'),
        ('forms', '0035_house_map_construction'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehiclePurchase',
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
            name='VehiclePurchaseLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('purchased_amount', models.IntegerField(verbose_name='खरिद संख्या')),
                ('price', models.FloatField(verbose_name='मूल्य')),
                ('remarks', models.CharField(max_length=300, verbose_name='कैफियत')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_data.governmentbody', verbose_name='विप्रयोग गर्नेपदाधिकारी र्सस्थावरण')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_data.vehicle', verbose_name='सवारी साधन')),
                ('vehiclepurchase_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='forms.vehiclepurchase')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
