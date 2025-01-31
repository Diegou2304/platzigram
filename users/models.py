from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=50, blank=True)

    #Seleccionamos donde queremos que se guarden nuestras imagenes
    picture = models.ImageField(upload_to='users/pictures',
                                blank=True,
                                null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username
