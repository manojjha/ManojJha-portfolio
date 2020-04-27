from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email =     models.EmailField() 
    subject =   models.CharField(max_length=1000)
    message = models.CharField(max_length=20000)
    phone = PhoneNumberField(null=False, blank=False, unique=False)


    def __str__(self):
        return self.email