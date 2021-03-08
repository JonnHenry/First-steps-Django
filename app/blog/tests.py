from config.wsgi import *
from blog.models import Categoria


categorias = Categoria.objects.all()  #Se accede a toda la información
"""
categoria = Categoria(nombre="Python 3 ")
categoria.save()
"""

categoriaPython = Categoria.objects.get(pk=1)
print(categoriaPython)