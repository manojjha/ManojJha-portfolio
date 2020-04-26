from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    views = models.PositiveIntegerField(default=0)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
