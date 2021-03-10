# Generated by Django 3.1.4 on 2021-02-22 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0037_additionalconvenience'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionalGrant',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(
                    auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(
                    auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('create_user', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConditionalGrantLine',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(
                    auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(
                    auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('total_grant', models.IntegerField(verbose_name='जम्मा अनुदान')),
                ('expense', models.FloatField(verbose_name='खर्च')),
                ('freeze_amount', models.FloatField(
                    verbose_name='बाँकि (फ्रिज हुनुपर्नें)')),
                ('remarks', models.CharField(max_length=300, verbose_name='कैफियत')),
                ('condtionalgrant_line', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='forms.conditionalgrant')),
                ('grant_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                 to='master_data.granttype', verbose_name='अनुदानको किसिम')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
