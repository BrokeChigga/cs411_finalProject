from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Actor(models.Model):
    name = models.CharField(max_length=2000)
    birth_date = models.CharField(max_length=2000, default = "")

    def __str__(self):
        return self.name

class DirectedBy(models.Model):
    movie_name = models.CharField(max_length=200, default = "")
    year = models.IntegerField(default = 1)
    director_name = models.CharField(max_length=200, default = "")
    def __str__(self):
        return self.movie_name + ' - ' + self.director_name


class Director(models.Model):
    name = models.CharField(max_length=200, default = "")
    birth_date = models.DateField

    def __str__(self):
        return self.name

class Has(models.Model):
    movie_name = models.CharField(max_length=200, default = "")
    movie_year = models.IntegerField(default = 1)
    reviewId = models.IntegerField(default = 1)


class Like(models.Model):
    email = models.CharField(max_length=200, default = "")
    movie_name = models.CharField(max_length=200, default = "")
    # movie_year = models.IntegerField(default = 1)

    def __str__(self):
        return self.email + ' - ' + self.movie_name

class Movie(models.Model):
    name = models.CharField(max_length=2000)
    year = models.IntegerField(default = 1)
    description = models.CharField(max_length=200, default = "")
    length = models.IntegerField(default = 1)
    #rating = models.CharField(max_length=2000, default="")
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=2000)

    def __str__(self):
        return self.name + ' - ' + self.category


class PlayedBy(models.Model):
    movie_name = models.CharField(max_length=2000)
    movie_year = models.IntegerField(default = 1)
    actor_name = models.CharField(max_length=2000)

    def __str__(self):
        return self.movie_name + ' - ' + self.actor_name


class Review(models.Model):
    email = models.CharField(max_length=2000, default="")
    reviewId = models.IntegerField(default = 1)
    date = models.DateField
    content = models.CharField(max_length=2000)

    def __str__(self):
        return self.email + ' - ' + self.content


class User(models.Model):
    email = models.CharField(max_length=2000)
    password = models.CharField(max_length=2000)

    def __str__(self):
        return self.email + ' - ' + self.password
