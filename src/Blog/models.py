from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    when = models.DateField()
    location = models.CharField(max_length=200)
    photo = models.ImageField(blank=True)
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    message = models.TextField()

