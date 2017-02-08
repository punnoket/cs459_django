from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    title=models.CharField(
        choices=(
            ('Mr', 'Mr'),
            ('Ms', 'Ms'),
            ),
        max_length=5,
        )
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    date_of_birth=models.DateField(blank=True)
    tel=models.CharField(max_length=13)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.first_name

class Car(models.Model):
    model=models.CharField(max_length=10)
    milage=models.FloatField(default=0.0)
    ppd=models.FloatField(default=0.0) #price per day
    image=models.FileField(upload_to='car_img',  blank=True)
    def __unicode__(self):
        return self.model

class Rent(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    car=models.ForeignKey(Car, on_delete=models.CASCADE)
    last_update=models.DateTimeField(auto_now_add=True)
    start=models.DateTimeField()
    stop=models.DateTimeField()
    def __unicode__(self):
        return str(self.pk)