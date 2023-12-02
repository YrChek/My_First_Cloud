# import datetime
import os
import hashlib
import shutil

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum, Count
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from my_first_cloud import settings
from my_first_cloud.settings import MEDIA_ROOT


def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.user.username, filename)


class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True)
    relative_path = models.CharField(max_length=255, blank=True)

    @property
    def files(self):
        obj = Files.objects.filter(user=self.pk)
        data = obj.aggregate(sum=Sum('size'), count=Count('id'))
        return data


class Files(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owners')
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


@receiver(pre_delete, sender=User)
def delete_user(sender, instance, **kwargs):
    files_path = instance.relative_path
    media_path = MEDIA_ROOT
    path = f'{media_path}{files_path}'
    if os.path.exists(path):
        shutil.rmtree(path)
        print('DELETE')
