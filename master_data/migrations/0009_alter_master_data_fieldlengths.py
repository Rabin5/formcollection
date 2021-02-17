# Generated by Django 3.1.4 on 2021-02-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0008_merge_20210211_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionplanactivity',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='allowancetype',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='committee',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='expenseheader',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='governmentbody',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='नाम'),
        ),
        migrations.AlterField(
            model_name='governmentbodytype',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='वर्णन'),
        ),
        migrations.AlterField(
            model_name='manpower',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='officebearer',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='procurementmethod',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='नाम'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='नाम'),
        ),
        # migrations.AlterField(
        #     model_name='province',
        #     name='name',
        #     field=models.CharField(max_length=300, unique=True, verbose_name='प्रदेश'),
        # ),
        migrations.AlterField(
            model_name='relieftype',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='sourcebudget',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='unitofmeasure',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='नाम'),
        ),
    ]
