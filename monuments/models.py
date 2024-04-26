# monuments/models.py

from django.db import models


class monument(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
