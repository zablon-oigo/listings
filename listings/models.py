from django.db import models
from django.utils.timezone import now
from datetime import datetime
from django.contrib.auth.models import User

class Listings(models.Model):
    class SaleType(models.TextChoices):
        PICK_UP="Available for pick up"
        SHIP="Available for shipping"
    
    class ConditionType(models.TextChoices):
        USED="Used"
        NEW="New"
    
    class ProductType(models.TextChoices):
        BIKE="Bike"
        PARTS="Parts"
        OTHER="Other"
    
    title = models.CharField(max_length=100)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    condition=models.CharField(max_length=40,choices=ConditionType.choices, default=ConditionType.USED)
    product_type=models.CharField(max_length=40,choices=ProductType.choices, default=ProductType.OTHER)
    sale_type=models.CharField(max_length=40,choices=SaleType.choices, default=SaleType.SHIP)
    price=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)
    main_photo=models.ImageField(upload_to="photos", blank=True)
    photo_1=models.ImageField(upload_to="photos", blank=True)
    photo_2=models.ImageField(upload_to="photos" ,blank=True)
    list_date=models.DateTimeField(default=now)
    contact_email=models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="Listings"