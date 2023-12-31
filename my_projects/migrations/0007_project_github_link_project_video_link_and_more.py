# Generated by Django 4.0.3 on 2023-12-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_projects', '0006_alter_project_used_technologies'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='video_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='website_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
