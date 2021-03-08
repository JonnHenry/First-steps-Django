from django.contrib import admin
from blog.models import Categoria,Post

# Register your models here.

admin.site.register([Categoria,Post]) #Para poder administrar los datos de Blog desde el panel de Administración
