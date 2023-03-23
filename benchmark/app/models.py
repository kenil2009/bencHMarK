from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

STATE_CHOICES =  (
    ('Andaman &  Nicobar Island','Andaman &  Nicobar Island'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Gujarat','Gujarat'),
    ('Maharashtra','Maharashtra'),
    ('New Delhi','New Delhi'),
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)
    
CATEGORY_CHOICES = (
    ('M','Mobile'),
    ('L','Laptop'),
    ('MW','Mens Wear'),
    ('WW','Womens Wear'),
)
class Product (models.Model):
    title = models. CharField (max_length=100) 
    selling_price = models. FloatField() 
    discounted_price = models. FloatField() 
    description = models. TextField() 
    brand= models.CharField (max_length=100) 
    category=models. CharField( choices=CATEGORY_CHOICES, max_length=2) 
    product_image = models. ImageField (upload_to='productimg') 
    
    def _str_(self):
         return str(self.id)
