# Generated by Django 4.2.4 on 2023-11-20 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_alter_job_company'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='job',
            unique_together={('position', 'company')},
        ),
    ]