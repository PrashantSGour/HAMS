# Generated by Django 4.2.6 on 2023-10-13 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mr',
            name='Demail',
        ),
        migrations.RemoveField(
            model_name='mr',
            name='Pemail',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='MR',
        ),
    ]
