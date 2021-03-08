from django.contrib import admin
from django.urls import path, include
from django.conf import settings #Para poder ver las imagenes desde el panel de administración
from django.conf.urls.static import static

# include to use the urls defined in the app blog specific in the file urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path('accounts/',include('auntenticacion.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#se realiza la configuración con static xq se cambio las urls donde se guardaba la configuración del archivo settings principal


