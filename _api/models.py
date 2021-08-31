from django.db import models

# Create your models here.

class Api(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_rating = models.CharField(max_length=10)
    movie_year = models.CharField(max_length=5)
    movie_duration = models.CharField(max_length=10)
    movie_description = models.CharField(max_length=700)

    def __str__(self):
        return f"{self.movie_name} - {self.movie_rating} - {self.movie_year}-{self.movie_duration}-{self.movie_description}"