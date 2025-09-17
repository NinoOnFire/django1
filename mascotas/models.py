from django.db import models

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
