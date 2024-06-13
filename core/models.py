import uuid

from django.db.models import Model, TextField, CharField, ImageField, URLField, DateTimeField, ForeignKey, CASCADE, \
    UUIDField, OneToOneField, EmailField, IntegerField
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field
from parler.models import TranslatableModel, TranslatedFields


class CreatedAtBase(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Base(CreatedAtBase):
    # id = UUIDField(primary_key=True, db_default=RandomUUID(), editable=False) # postgres da ishlatiladi
    id = UUIDField(default=uuid.uuid4, primary_key=True)  # sqlite uchun basic

    class Meta:
        abstract = True


class News(Base, TranslatableModel):
    translations = TranslatedFields(
        title=CharField(max_length=355),
        description=CKEditor5Field(),
    )

    class Meta:
        verbose_name_plural = "News"


class NewsImage(Base):
    news = ForeignKey('core.News', CASCADE, related_name='images')
    image = ImageField(upload_to='news/')


class Partner(Model):
    image = ImageField(upload_to='partners/')
    url = URLField(max_length=255)


class Expert(TranslatableModel):
    translation = TranslatedFields(
        full_name=CharField(max_length=255),
        description=TextField(),
        job=CharField(max_length=255)
    )

    image = ImageField(upload_to='expert/')
    website = OneToOneField('core.ExpertWebsite', CASCADE, null=True, blank=True,
                            related_name='experts')


class ExpertWebsite(Model):
    facebook = URLField(max_length=255, null=True, blank=True)
    linkedin = URLField(max_length=255, null=True, blank=True)
    messenger = URLField(max_length=255, null=True, blank=True)
    expert = OneToOneField("core.Expert", CASCADE, related_name='websites')


class Project(Base, TranslatableModel):
    translation = TranslatedFields(
        title=CharField(max_length=355),
        description=CKEditor5Field()
    )
    image = ImageField(upload_to='projects/')

    def __str__(self):
        return self.title


class Country(Model):
    title = CharField(max_length=100)

    def __str__(self):
        return self.title


class Study(Model):
    title = CharField(max_length=100)

    def __str__(self):
        return self.title


class Employee(Model):
    LANGUAGE = [
        (1, "Tanlang"),
        (2, "O'zbek tili"),
        (3, "Ingiliz tili"),
        (4, "Rus tili"),
    ]

    WORK_EXPERIENCE = [
        (1, "Tanlang"),
        (2, "1 yildan kam"),
        (3, "1 yildan ortiq"),
        (4, "3 yildan kam"),
        (5, "3 yildan ortiq"),
        (6, "5 yildan kam"),
        (7, "5 yildan ortiq"),
    ]

    TITLE = [
        (1, "Tanlang"),
        (2, "Dr."),
        (3, "Professor"),
        (4, "Mutaxassis"),
        (5, "Janob."),
        (6, "Miss"),
        (7, "Xonim.")
    ]

    CHOOSER_CHOICES = [
        (0, ""),
        (1, "Qisqa muddatga"),
        (2, "Uzoq muddatga"),
    ]

    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    email = EmailField(max_length=100)
    phone_number = CharField(max_length=50)
    language = IntegerField(choices=LANGUAGE, default=1)
    experience = IntegerField(choices=WORK_EXPERIENCE, default=1)
    title = IntegerField(choices=TITLE, default=1)
    duration = IntegerField(choices=CHOOSER_CHOICES, default=0)
    special_request = TextField()
    country = ForeignKey("core.Country", CASCADE)
    study = ForeignKey("core.Study", CASCADE)

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"


class Service(TranslatableModel):
    translation = TranslatedFields(
        title=CharField(max_length=255),
        description=CKEditor5Field()
    )
    image = ImageField(upload_to='service_icon/')


class AboutUs(TranslatableModel):
    translation = TranslatedFields(
        description=CKEditor5Field()
    )
    image = ImageField(upload_to='about_us/')


class OurWorks(TranslatableModel):
    translation = TranslatedFields(
        title=CharField(max_length=255),
        description=CKEditor5Field()
    )
    image = ImageField(upload_to='our_works/')


class Message(Base):
    full_name = CharField(max_length=255)
    email = EmailField()
    subject = CharField(max_length=255)
    message = TextField()
