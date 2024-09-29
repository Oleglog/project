# Generated by Django 5.1.1 on 2024-09-24 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_rename_descpiption_phone_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='headphones',
            name='description',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='headphones',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smart_watch',
            name='description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smart_watch',
            name='title',
            field=models.CharField(default=12, max_length=255),
            preserve_default=False,
        ),
    ]
