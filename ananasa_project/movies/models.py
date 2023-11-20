from django.db import models

# Create your models here.

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=100,blank=True)
    duration = models.IntegerField(blank=True)
    rating = models.FloatField(blank=True)
    
    # Add more fields as needed

    def __str__(self):
        return self.title
