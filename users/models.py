from django.db import models

# Create your models here.
class cuisines(models.Model):
    name = models.CharField(max_length=100)
    recepie = models.TextField()
    description = models.TextField()

class dance_froms(models.Model):
    name = models.CharField(max_length=100)
    origin = models.TextField()
    description = models.TextField()

class festivals(models.Model):
    name = models.CharField(max_length=100)
    importance = models.TextField()

class monuments(models.Model):
    name = models.CharField(max_length=100)
    buildingstyle = models.TextField()

class Fullname(models.Model):
    name = models.TextField()
