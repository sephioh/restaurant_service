from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100, blank=False, default=None)
    opens_at = models.TimeField()
    closes_at = models.TimeField()
