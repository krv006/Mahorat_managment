import uuid

from django.db import models
from django.db.models import Model, TextField, CharField, ImageField, URLField, DateTimeField, ForeignKey, CASCADE, \
    TextChoices
from django_ckeditor_5.fields import CKEditor5Field
from rest_framework.fields import EmailField


class CreatedAtBase(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

a
class Base(CreatedAtBase):
    # id = UUIDField(primary_key=True, db_default=RandomUUID(), editable=False) # postgres da ishlatiladi
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)  # sqlite uchun basic

    class Meta:
        abstract = True


class News(Base):
    title = CharField(max_length=355)
    description = TextField()


class NewsImage(Base):
    news = ForeignKey('core.News', CASCADE, related_name='images')
    image = ImageField(upload_to='news/')


class Media(Model):
    icon = CharField(max_length=255)
    url = URLField(max_length=255)


class Partner(Model):
    image = ImageField(upload_to='partners/')
    url = URLField(max_length=255)

    def __str__(self):
        return self.url


class Expert(Model):
    full_name = CharField(max_length=255)
    description = TextField()
    job = CharField(max_length=255)
    image = ImageField(upload_to='expert/')


class Website(Model):
    facebook = URLField(max_length=255, null=True, blank=True)
    linkedin = URLField(max_length=255, null=True, blank=True)
    messenger = URLField(max_length=255, null=True, blank=True)
    expert = ForeignKey('core.Expert', CASCADE, related_name='website')


class Worker(Base):
    full_name = CharField(max_length=50)
    job = CharField(max_length=55)
    image = ImageField(upload_to='workers/')

    def __str__(self):
        return self.full_name


class Project(Base):
    title = CharField(max_length=355)
    description = TextField()
    image = ImageField(upload_to='projects/')

    def __str__(self):
        return self.title


class Employee(Base):
    title = CharField(max_length=25)
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    email = EmailField(max_length=100)
    phone_number = CharField(max_length=50)
