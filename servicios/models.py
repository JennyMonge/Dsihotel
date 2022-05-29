from django.db import models
from base.models import BaseModel

# Create your models here.


class Servicios(BaseModel):
    nombre_servicio = models.CharField(
        'Nombre de Servicio',  max_length=100, blank=False, null=False)
    descripcion = models.TextField('Descripción', blank=False, null=False)
    precio = models.FloatField('Precio', blank=False, null=False)
    capacidad = models.CharField(
        'Capacidad', max_length=50, blank=False, null=False, default='')

    class Meta:
        verbose_name = ('Servicio')
        verbose_name_plural = ('Servicios')

    def __str__(self):
        return self.nombre_servicio



class Horarios(BaseModel):
    id_servicio = models.ForeignKey("Servicios", on_delete=models.CASCADE)
    d = (
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miercoles', 'Miercoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    )
    dias = models.CharField('Dia', max_length=50,
                            blank=False, null=False, choices=d)
    hora = models.CharField('Hora', max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = ('Horario')
        verbose_name_plural = ('Horarios')

    def __str__(self):
        return str(self.id) 

