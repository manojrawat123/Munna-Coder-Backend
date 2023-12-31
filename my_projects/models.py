from django.db import models

class Project(models.Model):
    PROJECT_TYPES = (
        ('Paid', 'Paid'),
        ('Practice', 'Practice'),
    )
    image = models.ImageField(upload_to='project_images/')
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=PROJECT_TYPES)
    category = models.CharField(max_length=10, choices=PROJECT_TYPES)
    description = models.TextField()
    associated_with = models.CharField(max_length=255) 
    subheading = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    cms = models.CharField(max_length=1000, blank=True, null=True)
    language_used = models.CharField(max_length=1000, blank=True, null=True)
    library_used = models.CharField(max_length=1000,blank=True, null=True)
    github_frontend_link = models.URLField(blank=True, null=True)
    github_backend_link = models.URLField(blank=True, null=True)
    website_link = models.URLField(blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.title
