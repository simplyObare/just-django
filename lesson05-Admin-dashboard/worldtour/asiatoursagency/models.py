from django.db import models


# Create your models here.
class Tour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"Tour ID: {self.id}, traveling from: {self.origin_country}, To: {self.destination_country}, number of nights: {self.number_of_nights} and cost of the tour: ${self.price}"
