# Generated by Django 3.2.5 on 2021-07-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Umbanda', max_length=255),
        ),
    ]
