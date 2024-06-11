<<<<<<< HEAD
# Generated by Django 5.0.6 on 2024-06-11 16:40

import django.db.models.deletion
import django_ckeditor_5.fields
import uuid
=======
# Generated by Django 5.0.6 on 2024-06-10 16:49

>>>>>>> ef18812b7247eac6e4355ec9d6b34ff93ba7b7c5
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_us/')),
                ('description', django_ckeditor_5.fields.CKEditor5Field()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('language', models.CharField(choices=[(1, 'Tanlang'), (2, "O'zbek tili"), (3, 'Ingiliz tili'), (4, 'Rus tili')], default=1, max_length=25)),
                ('experience', models.CharField(choices=[(1, 'Tanlang'), (2, '1 yildan kam'), (3, '1 yildan ortiq'), (4, '3 yildan kam'), (5, '3 yildan ortiq'), (6, '5 yildan kam'), (7, '5 yildan ortiq')], default=1, max_length=25)),
                ('title', models.CharField(choices=[(1, 'Tanlang'), (2, 'Dr.'), (3, 'Professor'), (4, 'Mutaxassis'), (5, 'Janob.'), (6, 'Miss'), (7, 'Xonim.')], default=1, max_length=25)),
                ('duration', models.CharField(choices=[(0, ''), (1, 'Qisqa muddatga'), (2, 'Uzoq muddatga')], default=0, max_length=25)),
                ('special_request', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('job', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='expert/')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=355)),
                ('description', django_ckeditor_5.fields.CKEditor5Field()),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='OurWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', django_ckeditor_5.fields.CKEditor5Field()),
                ('image', models.ImageField(upload_to='our_works/')),
=======
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=355)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='news/')),
>>>>>>> ef18812b7247eac6e4355ec9d6b34ff93ba7b7c5
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='partners/')),
                ('url', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
<<<<<<< HEAD
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=355)),
                ('description', django_ckeditor_5.fields.CKEditor5Field()),
                ('image', models.ImageField(upload_to='projects/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', django_ckeditor_5.fields.CKEditor5Field()),
                ('image', models.ImageField(upload_to='service_icon/')),
            ],
        ),
        migrations.CreateModel(
            name='ExpertWebsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, max_length=255, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=255, null=True)),
                ('messenger', models.URLField(blank=True, max_length=255, null=True)),
                ('expert', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='websites', to='core.expert')),
            ],
        ),
        migrations.AddField(
            model_name='expert',
            name='website',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experts', to='core.expertwebsite'),
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='news/')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.news')),
            ],
            options={
                'abstract': False,
            },
        ),
=======
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=355)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='projects/')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('work', models.CharField(max_length=55)),
                ('image', models.ImageField(upload_to='workers/')),
            ],
        ),
>>>>>>> ef18812b7247eac6e4355ec9d6b34ff93ba7b7c5
    ]
