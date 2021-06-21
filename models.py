from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    image=models.ImageField()
    title=models.CharField(max_length=40)
    slug=models.SlugField(max_length=40)
    description=models.TextField()
    price=models.IntegerField()

    def get_absulate_url(self):
        return reverse ("hello",kwargs={'slug':self.slug})

class Custemer(models.Model):
    name=models.CharField(max_length=40,null=True)
    mobileno=models.IntegerField(null=True)
    emailid=models.CharField(max_length=20,null=True)
    pin=models.IntegerField(null=True)
    houseno=models.CharField(max_length=40,null=True)
    area=models.CharField(max_length=40,null=True)
    landmark=models.CharField(max_length=40,null=True)
    city=models.CharField(max_length=40,null=True)
    state=models.CharField(max_length=40,null=True)
    totalprice=models.IntegerField(null=True)
