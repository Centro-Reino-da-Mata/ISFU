# Generated by Django 3.2.5 on 2021-09-02 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_remove_agenda_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='date_actividad',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Actividad'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='date_agenda',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
    ]
