# Generated by Django 4.2.5 on 2023-10-26 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_files_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owners', to=settings.AUTH_USER_MODEL),
        ),
    ]
