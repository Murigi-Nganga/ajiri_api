# Generated by Django 4.2.4 on 2023-11-18 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_company_alter_job_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.CharField(max_length=50),
        ),
    ]
