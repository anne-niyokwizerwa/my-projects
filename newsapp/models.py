from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='authors/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
        title = models.CharField(max_length=200)
        content = models.TextField()
        author = models.CharField(max_length=100)
        published_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.article}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return f"{self.name} ({self.email})"


class News(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    url = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title
class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title