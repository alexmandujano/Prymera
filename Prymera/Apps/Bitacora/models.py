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
		#inicio
class Evento(models.Model):
	NOMBRE=models.CharField( max_length=30)
	TIPO=models.CharField(max_length=2) #es para diferenciar los tipos
	def __unicode__(self):
		return self.NOMBRE

class Agencia(models.Model):
	CODIGO=models.CharField(max_length=4)
	NOMBRE=models.CharField(max_length=30)
	def __unicode__(self):
		return self.NOMBRE

class Proceso(models.Model):
	NOMBRE=models.CharField(max_length=50)
	TIPO=models.CharField(max_length=2)#es para diferenciar los tipos
	def __unicode__(self):
		return self.NOMBRE

class Factor(models.Model):
	NOMBRE=models.CharField( max_length=30)
	TIPO=models.CharField(max_length=2) #es para diferenciar los tipos
	def __unicode__(self):
		return self.NOMBRE
class Opcion_Comunicacion(models.Model):
	
	CATEGORIA=models.ForeignKey(Categoria)
	TIPO_EVENTO=models.ForeignKey(Evento)
	FACTOR=models.ForeignKey(Factor)
	
	def __unicode__(self):
		return self.CATEGORIA.NOMBRE+"/"+self.TIPO_EVENTO.NOMBRE+"/"+self.FACTOR.NOMBRE

#fin

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

#inicio
class Bitacora_Comunicacion(models.Model):
	TIPO_CAIDA=models.CharField(max_length=1)
	AGENCIA=models.ForeignKey(Agencia)
	USUARIO_A=models.CharField(max_length=15)
	USUARIO_S=models.CharField(max_length=15)
	FECHA_INICIO=models.DateField()
	FECHA_DESCUBRIMIENTO=models.DateField()
	FECHA_FIN=models.DateField()
	H_INICIO=models.TimeField()
	H_DESCUBRIMIENTO=models.TimeField()	
	H_FIN=models.TimeField()
	MEDIO=models.ForeignKey(Medio)
	TIPO_EVENTO=models.ForeignKey(Evento)
	OPCION=models.ForeignKey(Opcion_Comunicacion)
	PROCESO=models.ForeignKey(Proceso)
	DESCRIPCION1=models.CharField(max_length=80)
	DESCRIPCION2=models.CharField(max_length=80,blank=True,null=True)

	def __unicode__(self):
		return self.DESCRIPCION1
#fin

