# Generated by Django 3.1.5 on 2021-02-09 08:57

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_system_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='sessionyearmodel',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
