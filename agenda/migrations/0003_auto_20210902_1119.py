# Generated by Django 3.2.5 on 2021-09-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_alter_agenda_date_agenda'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='date_actividad',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Actividad'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='date_agenda',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
    ]
