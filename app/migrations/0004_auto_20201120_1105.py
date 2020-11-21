# Generated by Django 3.1.3 on 2020-11-20 14:05

import app.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_post_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hero',
            field=stdimage.models.StdImageField(blank=True, upload_to=app.models.get_file_path, verbose_name='Hero'),
        ),
    ]
