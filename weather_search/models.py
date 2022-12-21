from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    weather_data = models.JSONField()
    city_name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.city_name