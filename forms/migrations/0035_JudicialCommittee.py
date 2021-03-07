# Generated by Django 3.1.4 on 2021-02-25 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0034_teacherdesgination'),
    ]

    operations = [
        migrations.CreateModel(
            name='JudicialCommittee',
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
            name='JudicialCommitteeLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='सिर्जना मिति')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='अद्यावधिक मिति')),
                ('prev_remaining', models.FloatField(verbose_name='गतवर्षको बाँकी')),
                ('current_addition', models.FloatField(verbose_name='यसवर्ष थप')),
                ('total', models.FloatField(verbose_name='जम्मा')),
                ('summed_up', models.FloatField(verbose_name='यो वर्ष फछर्यौट')),
                ('remaining', models.FloatField(verbose_name='फछर्यौट हुन बाँकी')),
                ('desc', models.CharField(max_length=300, verbose_name='समयमै फछर्यौट नहुनुको कारण')),
                ('complaint_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_data.complainttype', verbose_name='उजुरीको प्रकार')),
                ('judicialcommittee_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='forms.judicialcommittee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]