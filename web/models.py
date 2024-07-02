from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.genero)

class Registro_cliente(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE) # username y contrasena
    fecha_nac   = models.DateField()
    id_genero   = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero')
    cel         = models.IntegerField()

    def __str__(self):
        return self.user.username