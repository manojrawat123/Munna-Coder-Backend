# Generated by Django 4.0.3 on 2023-12-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='technologies_used',
            field=models.JSONField(default={'languages': ['Python', 'JavaScript'], 'libraries': ['Django', 'React']}),
        ),
    ]
