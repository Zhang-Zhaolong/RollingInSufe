from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from article.models import Tag
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from mdx_math import MathExtension
import re


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Notebook(models.Model):
    notebook_name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    foreword = models.TextField(blank=True)
    abstract = models.CharField(max_length=20, blank=True)

    created_time = models.DateTimeField(default=timezone.now)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.notebook_name

    def save(self, *args, **kwargs):
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            MathExtension(enable_dollar_delimiter=True),
            # 'mdx_math',
            TocExtension(slugify=slugify),
        ])
        self.foreword = md.convert(self.foreword)
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)


class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    in_notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
