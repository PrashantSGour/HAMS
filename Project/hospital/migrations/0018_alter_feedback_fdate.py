# Generated by Django 4.2.6 on 2023-10-15 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0017_remove_feedback_ftime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='fdate',
            field=models.DateField(null=True),
        ),
    ]