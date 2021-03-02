# Generated by Django 3.1.4 on 2021-02-25 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0035_JudicialCommittee'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumerCommitteeConstructionDescription',
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
            name='ConsumerCommitteeConstructionDescriptionLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('program', models.TextField(verbose_name='कार्यक्रमको नाम')),
                ('total_expense', models.FloatField(verbose_name='निर्माण कार्यमा भएको कुल खर्च')),
                ('consumer_committee_expense', models.FloatField(verbose_name='कुल खर्च मध्ये उपभोक्ता समिति मार्फत भएको रकम')),
                ('construction_business_expense', models.FloatField(verbose_name='निर्माण व्यवसायीबाट भएको रकम')),
                ('consumercommitteeconstructiondescription_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='forms.consumercommitteeconstructiondescription')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
