# Generated by Django 4.2.6 on 2023-10-13 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0002_delete_staff'),
        ('Admin', '0006_remove_mr_demail_remove_mr_pemail_delete_appointment_and_more'),
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='Dpid',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]