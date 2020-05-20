from django.db import models
from django.core.validators import URLValidator
from django.conf import settings
import uuid
import base64


class Url(models.Model):
    url = models.CharField(max_length=256, validators=[URLValidator()])
    url_hash = models.CharField(max_length=16, unique=True, db_index=True)
    url_short = models.CharField(max_length=256, validators=[URLValidator()], blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def generate_hash(self):
        hash = base64.urlsafe_b64encode(uuid.uuid1().bytes)[:6]
        hash_exist = Url.objects.filter(url_hash=hash)
        while hash_exist:
            hash = base64.urlsafe_b64encode(uuid.uuid1().bytes)[:6]
            hash_exist = Url.objects.filter(url_hash=hash)
            continue
        hash = hash.decode('utf-8')
        return hash

    def create_short_url(self):
        return settings.HOST_NAME + self.url_hash

    def save(self, *args, **kwargs):
        self.url_hash = self.generate_hash()
        self.url_short = self.create_short_url()
        super(Url, self).save(*args, **kwargs)
