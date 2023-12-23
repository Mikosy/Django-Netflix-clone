from django.db import models
import uuid 
from django.utils import timezone
from django.conf import settings
# Create your models here.


class Movies(models.Model):

    class Meta:
        verbose_name_plural = "Movie"

    GENRE_CHOICES = {
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('science', 'Science Fiction'),
        ('fantasy', 'Fantasy'),
    }

    uu_id = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=150, choices=GENRE_CHOICES)
    length = models.PositiveIntegerField()
    image_card = models.ImageField(upload_to='movie_images/')
    image_cover = models.ImageField(upload_to='movie_images/')
    video = models.FileField(upload_to='movie_videos/')
    movie_views = models.IntegerField(default=0)
    parental_rating = models.CharField(max_length=50)
    created_date = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        return self.title
    

class MovieList(models.Model):

    class Meta:
        verbose_name_plural = "MovieList"


    owner_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner_user

