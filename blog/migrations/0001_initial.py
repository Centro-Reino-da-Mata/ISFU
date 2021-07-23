# Generated by Django 3.2.5 on 2021-07-20 22:39

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('correo', models.EmailField(max_length=200, verbose_name='Correo Electrónico')),
                ('asunto', models.CharField(max_length=100, verbose_name='Asunto')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='static/profile/images/')),
                ('facebook_url', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='static/post/images/')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('post_date', models.DateField(auto_now_add=True, null=True)),
                ('snippet', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
                ('likes', models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
