# Generated by Django 4.2.4 on 2023-08-16 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_students_dob_students_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]
