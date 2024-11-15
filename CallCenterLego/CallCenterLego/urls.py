from django.urls import path
from django.contrib import admin
from ModuloPeliculas import views  
from django.conf import settings
from django.conf.urls.static import static
from Online.views import Index, Inicio, RegisterView, LoginView, ViewRespuestas
from Administracion.views import IndexAdmin, BorrarPregunta, GestionUsuarios, EliminarUsuario, ModificarPregunta
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PeliculaListView, name='pelicula-list'),  # Vista de lista
    path('agregarpelicula/', views.agregar_pelicula, name='agregarpelicula'),  # Vista de agregar película
    path('pelicula/<int:id>/', views.pelicula_detail, name='pelicula-detail'),  # Vista de detalle de la película
    path('editar/<int:id>/', views.editar_pelicula, name='editar-pelicula'),  # Vista de editar película
    path('eliminar/<int:id>/', views.eliminar_pelicula, name='eliminar-pelicula'),  # Vista de eliminar película
    path('gestionpeliculas/', views.PeliculaListCrud, name='gestion_peliculas'),  # Vista de gestión de películas
    path('', Index),
    path('Administracion/', IndexAdmin),
    path('Login/', LoginView.as_view(), name='Login'),  # Cambiado a 'Login/'
    path('Register/', RegisterView.as_view(), name='Register'),
    path('Inicio/<int:id>', Inicio),
    path('Logout/', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('Respuesta/<int:idUser>/<int:idPregunta>', ViewRespuestas),
    path('BorrarPregunta/<int:idUser>/<int:idPregunta>', BorrarPregunta),
    path('GestionUsuarios/', GestionUsuarios),
    path('EliminarUsuario/<int:idUser>', EliminarUsuario),
    path('ModificarPregunta/<int:idPregunta>', ModificarPregunta)
]

# Para servir archivos multimedia durante el desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
