from django.db import models
import uuid

MOVIE_TYPE = (
    ('single', 'Single'),
    ('seasonal', 'Seasonal')
)


class Movie(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    type = models.CharField(max_length=10, choices=MOVIE_TYPE)
    videos = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers', blank=True, null=True)


class Video(models.Model):
    title = models.CharField(max_length=225, blank=True, null=True)
    file = models.FileField(upload_to='movies')
