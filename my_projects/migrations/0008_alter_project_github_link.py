# Generated by Django 4.0.3 on 2023-12-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_projects', '0007_project_github_link_project_video_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='github_link',
            field=models.URLField(default='github.com/manojrawat/'),
        ),
    ]
