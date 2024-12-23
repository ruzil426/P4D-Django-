from django.db import models
#
# # Create your models here.
# class City(models.Model):
#     city = models.CharField(max_length=25)

class City(models.Model):
    name = models.CharField(max_length=25)
    temperature = models.FloatField()
    temperature_feels = models.FloatField()
    humidity = models.CharField
    visibility = models.CharField
    description = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name