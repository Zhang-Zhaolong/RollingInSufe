from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    abstract = models.CharField(max_length=300, blank=True)
    body = models.TextField()

    created_time = models.DateTimeField(default=timezone.now)
    modified_time = models.DateTimeField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        self.abstract = self.body[:150] + '...'
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article:details', kwargs={'pk': self.pk})

