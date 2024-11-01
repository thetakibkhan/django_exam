from django.db import models

class Event(models.Model):
  title = models.CharField(max_length=255)
  date = models.DateField(null=True)
  location = models.CharField(max_length=255)