# Generated by Django 4.0.3 on 2023-12-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_projects', '0005_remove_project_technologies_used_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='used_technologies',
            field=models.JSONField(),
        ),
    ]
