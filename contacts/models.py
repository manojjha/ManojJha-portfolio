from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    name = models.EmailField()
    email =     models.EmailField() 
    subject =   models.CharField(max_length=1000)
    message = models.CharField(max_length=20000)
    document = models.FileField(upload_to='static/', blank=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)


    def __str__(self):
        return self.email