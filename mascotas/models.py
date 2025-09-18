from django.db import models
from django.contrib.auth.models import User

class Mascotas(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto= models.ImageField()

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.raza, self.descripcion)
    
    class Meta():
        db_table = 'mascota'
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'



class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    edad = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username