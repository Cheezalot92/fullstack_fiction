# Generated by Django 4.2.6 on 2023-10-18 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='name',
            new_name='title',
        ),
    ]