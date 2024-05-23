from django.db import models
from django.utils import timezone


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    duration = models.IntegerField()
    synopsis = models.TextField()

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.capacity})"


class FeatureFilm(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.movie} - {self.room}"


class Ticket(models.Model):
    feature_film = models.ForeignKey('FeatureFilm', on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.feature_film} - ${self.price} [{self.seat_number}]"
