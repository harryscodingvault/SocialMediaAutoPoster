from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=264, verbose_name='Make a title')
    slug = models.SlugField(max_length=264, unique=True)
    blog_content = models.TextField(verbose_name='What is on your mind?')
    blog_image = models.FileField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.blog_title


class BlogImages(models.Model):
    blog = models.ForeignKey(Blog, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='blog_images/')

    def __str__(self):
        return self.blog.blog_title