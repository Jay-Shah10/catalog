from django.db import models


# Create your models here.
class Genre(models.Model):
    genre = models.fields.CharField(max_length=100, default='')

    def __str__(self):
        return self.genre

class Movie(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.fields.CharField(max_length=100, default='')
    description = models.TextField()
    year = models.fields.CharField(max_length=4)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title
    