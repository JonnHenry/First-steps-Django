from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #Para proteger las rutas en caso de que no este logueado

from blog.forms import FormularioPost
from blog.models import Post

@login_required(login_url='/accounts/acceder')
def index(request):
    listado_posts = Post.objects.all()#Se obtienen todos los posts
    paginator = Paginator(listado_posts,3)# Se utiliza el paginador para q solo obtenga 3 posts
    pagina = request.GET.get('page') or 1 #Si se tiene la variable paginator cargar dicha variable sino por defecto usar 1
    posts = paginator.get_page(pagina) #Se obtinen los post de acuerdo a la pagina
    pagina_actual = int(pagina) #Se castea a int para evitar problemas
    paginas = range(1,posts.paginator.num_pages+1) #Se crea las paginas en un rango definido solo para mostrar
    return render(request, "blog.html",{"posts": posts,"paginas": paginas,"pagina_actual": pagina_actual}) #Se manda a renderizar la vista

@login_required(login_url='/accounts/acceder')
def crear_post(request):
    if request.method == "POST":
        form = FormularioPost(request.POST, request.FILES)  # Recibe los archivos con "FILES" y los datos del POST
        if (form.is_valid()):
            post = form.save(commit=False)#No se le hace todavia un commit con los datos a la base de datos
            post.autor_id = request.user.id # Se obtiene el id del autor
            post.save() #Se guarda el formulario que se recibe desde el front
            titulo = form.cleaned_data.get("titulo")
            messages.success(request, F'El post {titulo} se ha creado correctamente')
            return redirect("blog")
        else:
            for msg in form.errors:
                messages.error(request, form.errors[msg])

    form = FormularioPost()
    return render(request, "crear_post.html", {"form": form})


@login_required(login_url='/accounts/acceder') #Para asegurarse que el usuario tenga permisos para acceder
def eliminar_post(request,post_id):
    try:
       post =  Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        messages.error(request, "El post que deseas eliminar no existe")
        return redirect("blog")

    if post.autor != request.user:
        messages.error(request, "No eres el autor de este post")
    else:
        post.delete()
        messages.success(request,f"El post {post.titulo} se ha eliminado con éxito")
    return redirect("blog")



