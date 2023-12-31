from django.db import models

class ChatBotData(models.Model):
    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    ]

    name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,null=True)
    service_interested = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.name
