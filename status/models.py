from django.db import models

# Create your models here.
class Status(models.Model):
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_name