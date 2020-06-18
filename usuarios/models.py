from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class usuario(AbstractUser):
    id = models.AutoField(primary_key=True)

    email = models.EmailField(unique=True)
    celular = PhoneNumberField(null=True,blank=True)
    descripcion = models.TextField(max_length=1000,blank=True,null=True)
    foto = models.ImageField(upload_to='profile', blank=True, null=True)  
    def __str__(self):                                                                               
        return self.email