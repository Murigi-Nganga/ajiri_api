# Generated by Django 4.2.4 on 2023-11-18 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='title',
            new_name='position',
        ),
    ]
