# Generated by Django 3.1.4 on 2021-01-18 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0017_alter_line_inheritance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rdttestdetailline',
            name='create_user',
        ),
    ]