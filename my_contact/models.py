from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name
