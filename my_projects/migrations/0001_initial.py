# Generated by Django 4.0.3 on 2023-12-09 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_images/')),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('Paid', 'Paid'), ('Practice', 'Practice')], max_length=10)),
                ('category', models.CharField(choices=[('Paid', 'Paid'), ('Practice', 'Practice')], max_length=10)),
                ('description', models.TextField()),
                ('associated_with', models.CharField(max_length=255)),
                ('subheading', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]