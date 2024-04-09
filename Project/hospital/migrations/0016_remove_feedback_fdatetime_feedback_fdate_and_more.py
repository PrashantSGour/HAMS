# Generated by Django 4.2.6 on 2023-10-15 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0015_remove_feedback_id_feedback_fid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='fdatetime',
        ),
        migrations.AddField(
            model_name='feedback',
            name='fdate',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='ftime',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
    ]
