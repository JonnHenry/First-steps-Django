from django.db import models
from django.contrib.auth.models import User #Modelo que representa a la tabla auth user
import os

#Una clase se convierte en modelo de la base de datos
#Con la clase se convierte en modelo y poder representar a una tabla en la base de datos
class Categoria(models.Model):
    #Nombre es la etiqueta de este campo en un formulario
    nombre = models.CharField(max_length=100,null=False,unique=True,verbose_name='Nombre')

    def __str__(self): #Devuelve el nombre de la clase en String devolviendo 'Nombre' y no Object type Model
        return self.nombre

    #Cuando la clase se crea se crea la tabla como "categories"
    class Meta: #Son los metadatos
        db_table = 'categories' #Nombre de la tabla remplace the name blog_categories
        verbose_name = "Categoria" #Mostrar el nombre en singular
        verbose_name_plural = "Categorias" #Mostrar el nombre en plural
        ordering = ['id'] #Se ordena ascendentemente por el id, si se desea ordenar descendetemente se pone "-id"


class Post(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100,unique=True,null=False,verbose_name='Título')
    contenido = models.TextField(null=True,verbose_name='Contenido del post')
    imagen = models.ImageField(upload_to='posts/%Y/%m/%d',null=True,blank=True,verbose_name="Imagen del post") #Pillow es necesario para trabajar con imagenes
    fecha_alta = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de alta')
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualización')


    def __str__(self):
        return self.titulo #Retorna el titulo del post

    def delete(self, *args,**kwargs):
        if (os.path.isfile(self.imagen.path)):
            os.remove(self.imagen.path)
        super(Post,self).delete(*args,**kwargs) #Para sobrescribir el método delete predefinido

    class Meta: #Son los metadatos
        db_table = 'posts' #Nombre de la tabla remplace the name blog_categories
        verbose_name = "Post" #Mostrar el nombre en singular
        verbose_name_plural = "Posts" #Mostrar el nombre en plural
        ordering = ['id'] #Se ordena ascendentemente por el id, si se desea ordenar descendetemente se pone "-id"



