from django.shortcuts import render,redirect
from datetime import datetime
from Online.forms import RegisterForm,LoginForm,PreguntasForm,RespuestaForm
from django.views.generic import CreateView, FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from Online.models import Preguntas,Usuario, Respuesta

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'Register.html'
    success_url = '/Inicio/'
    succes_message = "%(name)s Se ha creado exitosamente!"
    def form_valid(self, form):
        print(len(self.request.POST['rut']))
        request = self.request
        login(request, form.save())
        if request.user.admin:
                return redirect('/Administracion/')
        return redirect('/Inicio/' + str(request.user.id))
class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/Inicio/'
    succes_message = "%(name)s Se ha creado exitosamente!"

    def form_valid(self, form):
        request = self.request
        Usuario = form.cleaned_data.get("Usuario")
        password = form.cleaned_data.get("password")
        remember_me = form.cleaned_data['remember_me']
        user = authenticate(request, username=Usuario, password=password)
        if user is not None:
            login(request, user)
            if not remember_me:
                            request.session.set_expiry(0)
            if user.admin or user.tecnico:
                return redirect('/Administracion/')
            return redirect('/Inicio/' + str(user.id))
        return super(LoginView, self).form_invalid(form)

def Index(request):
    return render(request, "index.html")
@login_required()
def Inicio(request, id):
    User = Usuario.objects.get(id=id)
    preguntas = Preguntas.objects.filter(Usuario=User)
    now = datetime.now()
    form = PreguntasForm(initial={'Usuario': id},)
    if request.method == "POST":
        guardarPregunta = Preguntas(Titulo=request.POST["Titulo"],Pregunta=request.POST["Pregunta"],Usuario=User, Fecha_creacion=now)
        guardarPregunta.save()
        return redirect('/Inicio/' + str(id))
    return render(request, "inicio.html", {"Preguntas":preguntas,"form":form,"id":id})

def ViewRespuestas(request,idUser,idPregunta):
    pregunta = Preguntas.objects.get(idPregunta=idPregunta)
    User = Usuario.objects.get(id=idUser)
    now = datetime.now()
    MostrarRespuestas = Respuesta.objects.filter(id_Pregunta=pregunta)
    form = RespuestaForm(initial={'id_Pregunta': idPregunta,'Usuario': pregunta.Usuario.id},)
    if request.method == "POST":
        guardarRespuesta = Respuesta(Respuesta=request.POST["Respuesta"], id_Pregunta=pregunta, Usuario=User, FechaHora=now)
        guardarRespuesta.save()
        return redirect('/Respuesta/' + str(idUser) +  "/" + str(idPregunta))

    return render(request,"Respuestas.html",{"Pregunta":pregunta,"form":form,"Respuestas":MostrarRespuestas})