from django.db import models


# Create your models here.
class Genre(models.Model):
    genre = models.fields.CharField(max_length=100, default='')

    def __str__(self):
        return self.genre


