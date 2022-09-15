from django.db import models

class Url(models.Model):
    long_url = models.CharField(max_length=8192)
    url_short_id = models.CharField(max_length=12)
    created_date = models.DateField('date published')