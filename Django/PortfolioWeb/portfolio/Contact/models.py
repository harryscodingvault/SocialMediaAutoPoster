from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=400, blank=False)
    message = models.TextField(max_length=800, blank=False)

    def __str__(self):
        return self.name
