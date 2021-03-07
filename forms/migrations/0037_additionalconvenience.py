# Generated by Django 3.1.4 on 2021-02-22 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0036_house_map_construction'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalConvenience',
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
            name='AdditionalConvenienceLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('conveniece_staff_count', models.IntegerField(verbose_name='सुविधा उपयोगको संख्या कर्मचारी')),
                ('convenience_officer_count', models.IntegerField(verbose_name='सुविधा उपयोगको संख्या पदाधिकारी')),
                ('yearly_expense', models.FloatField(verbose_name='बार्षिक खर्च')),
                ('remarks', models.CharField(max_length=300, verbose_name='कैफियत')),
                ('additionalconvenction_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line', to='forms.additionalconvenience')),
                ('convenience_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='master_data.conveniencetype', verbose_name='सुविधाको किसिम')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]