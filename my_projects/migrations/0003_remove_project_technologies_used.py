# Generated by Django 4.0.3 on 2023-12-09 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_projects', '0002_project_technologies_used'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='technologies_used',
        ),
    ]
