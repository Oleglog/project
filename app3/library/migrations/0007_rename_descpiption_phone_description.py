# Generated by Django 5.1.1 on 2024-09-24 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_phone_descpiption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='descpiption',
            new_name='description',
        ),
    ]
