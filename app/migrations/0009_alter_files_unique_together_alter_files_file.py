# Generated by Django 4.2.5 on 2023-10-16 16:34

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_files_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='files',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(unique=True, upload_to=app.models.user_directory_path),
        ),
    ]
