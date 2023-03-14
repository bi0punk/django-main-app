from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User


class Sismo(models.Model):
    local_date_cl = models.CharField(max_length=100)
    place = models.TextField()
    fecha_utc = models.TextField()
    earthquake_latitude = models.TextField()
    earthquake_longitude = models.TextField()
    earthquake_deep = models.TextField()
    magnitude = models.TextField()

    class Meta:
        verbose_name_plural = "sismos"

    def __str__(self): """
        return self.short_name """

