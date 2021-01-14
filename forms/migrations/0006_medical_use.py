# Generated by Django 3.1.4 on 2021-01-13 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0009_procurementmethod'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0005_medical_use'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master_data.governmentbody', verbose_name='निकायको नामः: ')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('fiscal_year', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='medical_use', to='master_data.fiscalyear', verbose_name='आर्थिक बर्ष: ')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MedicalUseLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('is_purchased', models.BooleanField(default=False, verbose_name='खरिद ')),
                ('product_price', models.FloatField(verbose_name='सामानको मुल्य')),
                ('unused_qty', models.IntegerField(verbose_name='प्रयोगमा नआएको परिमाण')),
                ('unused_reason', models.CharField(max_length=300, verbose_name='प्रयोगमा नआएको कारण')),
                ('remarks', models.CharField(max_length=300, verbose_name='कैफियत')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('medical_use_line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='forms.medicaluse')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master_data.product', verbose_name='स्वास्थ्य सामाग्री उपकरणको विवरण')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
