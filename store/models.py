from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    image = models.ImageField(default='car.jpg', upload_to='car_images')
    purchase_year = models.IntegerField()
    ex_price = models.FloatField()
    kms_driven = models.IntegerField()
    no_owners = models.IntegerField()
    fuel_type = models.CharField(max_length=25)
    engine = models.IntegerField()
    seats = models.IntegerField()
    transmission = models.CharField(max_length=25)
    seller_type = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.car_name} {self.purchase_year}'
