# visitors/models.py
from django.db import models

class Visitor(models.Model):
    # ip_address = models.GenericIPAddressField()
    sup_id_adress = models.CharField(max_length=200, null=True)
    visit_timestamp = models.DateTimeField(auto_now_add=True)
    location = models.TextField(null=True)
    website_accessed = models.CharField(max_length=200)
