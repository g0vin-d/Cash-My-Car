from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    image = models.ImageField(default='car.jpg', upload_to='car_images')
    purchase_year = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    ex_price = models.FloatField()
    kms_driven = models.IntegerField()
    no_owners = models.IntegerField()
    fuel_type = models.CharField(max_length=25)
    engine = models.IntegerField()
    seats = models.IntegerField()
    transmission = models.CharField(max_length=25)
    seller_type = models.CharField(max_length=25)
    car_type = models.CharField(max_length=10)
    selling_price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.car_name} {self.purchase_year}'

    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'pk': self.pk})
