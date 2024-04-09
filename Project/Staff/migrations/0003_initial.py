# Generated by Django 4.2.6 on 2023-10-13 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Doctor', '0003_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Staff', '0002_delete_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=50)),
                ('Sgender', models.CharField(choices=[('Male', 'M'), ('Female', 'F')], max_length=6)),
                ('Saddresss', models.CharField(max_length=100)),
                ('Sphone', models.PositiveIntegerField()),
                ('Sdob', models.DateField(max_length=8)),
                ('Semail', models.EmailField(max_length=254)),
                ('Spassword', models.CharField(max_length=30)),
                ('Sjob', models.CharField(max_length=50)),
                ('Ssalary', models.PositiveIntegerField()),
                ('Dpid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.department')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]