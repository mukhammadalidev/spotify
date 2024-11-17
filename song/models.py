from django.db import models

from users.models import CustomUser


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    source = models.FileField(upload_to="songs/")
    poster = models.ImageField(upload_to="songs/")

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="artist/")
    def __str__(self):
        return self.name

class PlayList(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PlayListSong(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    playlist = models.ForeignKey(PlayList, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)