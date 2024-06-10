from django.db import models
from django.db.models import Model


class News(models.Model):
    title = models.CharField(max_length=355)
    description = models.TextField()
    image = models.ImageField(upload_to='news/')


class Media(models.Model):
    icon = models.CharField(max_length=255)
    url = models.URLField(max_length=255)


class Partner(models.Model):
    image = models.ImageField(upload_to='partners/')
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.url


class Worker(models.Model):
    full_name = models.CharField(max_length=50)
    work = models.CharField(max_length=55)
    image = models.ImageField(upload_to='workers/')

    def __str__(self):
        return self.full_name


class Project(models.Model):
    title = models.CharField(max_length=355)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title


