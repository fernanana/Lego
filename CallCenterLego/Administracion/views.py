from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Online.models import Preguntas,Usuario
from Online.forms import PreguntasForm
@login_required()
def IndexAdmin(request):
    ListaPreguntas = Preguntas.objects.all()

    return render(request, "indexAdmin.html", {"Preguntas":ListaPreguntas})

def BorrarPregunta(request, idUser, idPregunta):
    User = Usuario.objects.get(id=idUser)
    if User.admin:
        Pregunta = Preguntas.objects.get(idPregunta=idPregunta)
        Pregunta.delete()
        return redirect("/Administracion/")
    else:
        if User.tecnico:
            return redirect("/Administracion/")
        return redirect("/Inicio/" + str(User.id))
@login_required()
def GestionUsuarios(request):
    Usuarios = Usuario.objects.all()
    if request.method == "POST":
        user = request.POST.get('Userid', False)
        activo = request.POST.get('activo', False)
        admin = request.POST.get('admin', False)
        tecnico = request.POST.get('tecnico', False)
        if admin:
            admin = True
        if activo:
            activo = True
        if tecnico:
            tecnico = True
        print(request.POST.get('Elimnar_user', False))
        userchange = Usuario.objects.get(id=user)
        userchange.admin = admin
        userchange.activo = activo
        userchange.tecnico = tecnico
        userchange.save()
        return redirect('/GestionUsuarios/')
    return render(request, "GestionUsuarios.html",{"Usuarios":Usuarios})
@login_required()
def EliminarUsuario(request,idUser):
    if request.user.admin:
        User = Usuario.objects.get(id=idUser)
        User.delete()
    return redirect('/GestionUsuarios/')
def ModificarPregunta(request,idPregunta):
    Pregunta = Preguntas.objects.get(idPregunta=idPregunta)
    form = PreguntasForm(instance=Pregunta)
    if request.method == 'POST':
        form = PreguntasForm(request.POST, instance=Pregunta)
        if form.is_valid():
            form.save()
        return redirect('/Administracion/')
    return render(request, "ModificarPregunta.html", {"form":form})
