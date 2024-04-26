# monuments/models.py

from django.db import models


class cuisines(models.Model):
    name = models.CharField(max_length=100)
    recepie = models.TextField()
    description = models.TextField()
