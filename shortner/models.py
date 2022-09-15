from django.db import models
from datetime import date, datetime


class Url(models.Model):
    long_url = models.CharField(max_length=8192)
    url_short_id = models.CharField(max_length=12)
    created_date = models.DateTimeField(default=datetime.now(), blank=None, null=None)