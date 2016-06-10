from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria (models.Model):
	NOMBRE=models.CharField(max_length=30)
	def __unicode__(self):
		return self.NOMBRE


class Sub_categoria (models.Model):
	NOMBRE=models.CharField(max_length=30)
	def __unicode__(self):
		return self.NOMBRE

class Detalle_Scategoria(models.Model):
	NOMBRE=models.CharField(max_length=30)
	def __unicode__(self):
		return self.NOMBRE

class Herramienta(models.Model):
	NOMBRE=models.CharField(max_length=30)
	def __unicode__(self):
		return self.NOMBRE 
class Opcion(models.Model):
	
	CATEGORIA=models.ForeignKey(Categoria)
	SUB_CATEGORIA=models.ForeignKey(Sub_categoria)
	DETALLE_SCATEGORIA=models.ForeignKey(Detalle_Scategoria)
	HERRAMIENTA=models.ForeignKey(Herramienta)

	def __unicode__(self):
		return self.CATEGORIA.NOMBRE+"/"+self.SUB_CATEGORIA.NOMBRE+"/"+self.DETALLE_SCATEGORIA.NOMBRE+"/"+self.HERRAMIENTA.NOMBRE

class Medio(models.Model):
	
	NOMBRE=models.CharField(max_length=30)
	def __unicode__(self):				
		return self.NOMBRE

class Estado(models.Model):
	
	NOMBRE=models.CharField(max_length=30)
	def __unicode__(self):
		return self.NOMBRE

class Bitacora(models.Model):
	FECHA=models.DateField()
	FECHA_ENVIO=models.DateField()
	H_RECEPCION=models.TimeField()	
	H_INICIO=models.TimeField()
	H_FIN=models.TimeField()
	ASUNTO=models.TextField()
	DETALLLE=models.TextField()
	USUARIO_S=models.CharField(max_length=15)
	USUARIO_R=models.CharField(max_length=15)
	USUARIO_A=models.CharField(max_length=15)
	USUARIO=models.CharField(max_length=15)
	ESTADO=models.ForeignKey(Estado)
	MEDIO=models.ForeignKey(Medio)
	OPCION=models.ForeignKey(Opcion)
	OTRA_AREA=models.CharField(max_length=1)
	
	def __unicode__(self):
		return self.ASUNTO





