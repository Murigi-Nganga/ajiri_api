# Generated by Django 4.2.4 on 2023-11-20 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0005_alter_applicant_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='resume',
        ),
        migrations.AddField(
            model_name='applicant',
            name='resume_file_path',
            field=models.CharField(default='example', max_length=300),
        ),
    ]
