from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .managers import TeacherManager
from uuid import uuid4

    # funcao para subir arquivo de foto unico do usuario avitando arquivos com 
    # mesmo nome serem sobreescrito
def get_unique_filename(instance, filename):
    return f"profile-images/{uuid4()}-{filename}"


# para sobreescrever o modelo de usuario do django e criar 
# a propria classe é necessário importar AbstractBaseUser
# PermissionsMixin serve para perimitir adicionar algumas
# partes das permissões do django

class Teacher(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=255)
    age = models.PositiveIntegerField(null=True)
    description = models.TextField(null=True)
    hourly_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    data_joined = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(null=True, upload_to=get_unique_filename)

    # como estou def. nossa usuario e preciso passar esse campo
    # defino qual campo vai ser usuario
    USERNAME_FIELD = "email"
    #defino campos obrigatorios
    REQUIRED_FIELDS = ["name"]

    objects = TeacherManager()

    def __str__(self):
        return self.email










