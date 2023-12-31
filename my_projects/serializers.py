from rest_framework import serializers
from my_projects.models import Project


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "image", "title", "type", "category", "description", "associated_with", "subheading", "slug", "cms", "language_used", "library_used", "github_frontend_link", "github_backend_link", "website_link", "video_link"]


