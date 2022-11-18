from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    name = models.CharField(max_length=50)
    profile_path = models.CharField(max_length=100, null=True)

class Director(models.Model):
    name = models.CharField(max_length=50)
    profile_path = models.CharField(max_length=100, null=True)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    actor = models.ManyToManyField(Actor)
    director = models.ManyToManyField(Director)
    

class MovieComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='user', on_delete=models.CASCADE )
    comment = models.TextField()
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    movie = models.ForeignKey(Movie, related_name='comment', on_delete=models.CASCADE, null=True)
    # commentcomment = models.ForeignKey('self', related_name='comment_comment', on_delete=models.CASCADE, null=True)


# 무비 코멘트와 댓글 코멘트 따로

class CommentReply(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='reply_user', on_delete=models.CASCADE )
    comment = models.TextField()
    moviecomment = models.ForeignKey(MovieComment, related_name='replymoviecomment', on_delete=models.CASCADE, null=True)
    parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE, null=True)