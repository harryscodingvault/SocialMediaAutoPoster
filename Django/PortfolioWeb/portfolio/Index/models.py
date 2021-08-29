from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to='about/', blank=False)

    def __str__(self):
        return self.title

class Skills(models.Model):
    language = models.CharField(max_length=100, blank=True)
    framework = models.CharField(max_length=100, blank=True)
    technology = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return  f'{self.language} {self.framework} {self.technology}'


class Intro(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800, blank=False)

    def __str__(self):
        return self.title


class Social(models.Model):
    site = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=400, blank=False)
    image = models.ImageField(upload_to='about/', blank=False)

    def __str__(self):
        return self.site


class Projects(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to='about/', blank=True)
    link = models.CharField(max_length=400, blank=False)
    is_big = models.BooleanField(blank=False)
    tags = models.TextField(max_length=800, blank=False)

    def __str__(self):
        return self.title

