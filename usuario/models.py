from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
    TIPOS_USUARIO = (
        ('I', 'Inquilino'),
        ('P', 'Proprietário'),
    )
    email = models.EmailField(unique=True)
    tipo = models.CharField(max_length=1, choices=TIPOS_USUARIO, default='I')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email