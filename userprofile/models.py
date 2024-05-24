from django.db import models
from django.contrib.auth.models import User
import os


def user_directory_path(instance, filename):
    ext = filename.split('.').pop()
    filename = '{0}{1}.{2}'.format(instance.user, instance.telephone, ext)
    return os.path.join(instance.major, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension')
    telephone = models.CharField(max_length=11)
    birthday = models.DateField(null=True, blank=True)
    major = models.CharField(blank=True, max_length=30)
    school = models.CharField(blank=True, max_length=30)
    photo = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            print(self.photo.url)
            return self.photo.url
        else:
            print(self.photo.url)


