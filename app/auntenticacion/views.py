from django.contrib import messages  # Importar los mensajes
from django.contrib.auth import login, logout,authenticate
# Formulario de Django para crear usuarios y esta vinculado con la tabla de la base de datos de Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import View


def acceder(request):
    if request.method=="POST":
        form = AuthenticationForm(request,data=request.POST)
        if (form.is_valid()):
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario,password=password)
            if (usuario is not None):
                login(request,usuario)
                messages.success(request, F"Bienvenid@ a la plataforma {nombre_usuario}")
                login(request, usuario)
                return redirect("blog")
            else:
                messages.error(request, "Los datos ingresados son incorrectos")
        else:
            messages.error(request, "Los datos ingresados son incorrectos")


    #Comprobar el usario
    form = AuthenticationForm()
    return render(request, "acceder.html", {"form": form})


# Definir metodos
class VistaRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro.html", {"form": form})

    def post(self, request):  # Metodo que espera campos
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            usuario = form.save()  # Crear un usuario en la tabla
            nombre_usuario = form.cleaned_data.get("username")
            messages.success(request, F"Bienvenid@ a la plataforma {nombre_usuario}")
            login(request, usuario)
            return redirect("blog")

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro.html", {"form": form})


def salir(request):
    logout(request)
    messages.success(request, F"Tu sesión se ha cerrado correctamente")
    return redirect("acceder")

# Create your views here.
