# import datetime
import os
import hashlib

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from my_first_cloud import settings


def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.user.username, filename)


class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True)
    relative_path = models.CharField(max_length=255, blank=True)


class Files(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    file = models.FileField(upload_to=user_directory_path)
    filename = models.CharField(max_length=255)
    url_hash = models.URLField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    download_date = models.DateField(null=True, blank=True)  # при создании прописывать null, просто '' не подходит
    size = models.IntegerField(default=0)
    type = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # dt_now = datetime.datetime.now()
        # str_dt_now = str(dt_now)
        # url_files = user_directory_path(self, self.filename) + str_dt_now
        url_files = user_directory_path(self, self.filename)
        if not self.pk:
            self.url_hash = hashlib.md5(url_files.encode()).hexdigest()
        return super().save(*args, **kwargs)


@receiver(pre_delete, sender=Files)
def delete_file(sender, instance, **kwargs):
    file_path = instance.file.path
    if os.path.exists(file_path):
        os.remove(file_path)
