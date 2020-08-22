from django.db import models

# Create your models here.
class Destination1(models.Model):

    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    decs = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)