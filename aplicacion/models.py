from django.db import models
from django.utils import timezone

class Encuesta(models.Model):
        autor = models.ForeignKey('auth.User')
        nombre = models.CharField(max_length=200)
        fecha_creacion = models.DateTimeField(
                blank=True, null=True)
        universo = models.IntegerField(default=0)

        def publish(self):
        	self.fecha_creacion = timezone.now()
        	self.save()
        
        def __str__(self):
            return self.nombre
