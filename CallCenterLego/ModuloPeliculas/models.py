from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Pelicula(models.Model):
    SUCURSAL_CHOICES = [
        ('PlazaOeste', 'Plaza Oeste'),
        ('MallAraucoMaipu', 'Mall Arauco Maipu'),
        ('CinepolisMaipu', 'Cinepolis Maipu'),
        ('PlazaOeste', 'Plaza Oeste'),
        ('PlazaVespucio', 'Plaza Vespucio'),
    ]
    GENERO_CHOICES = [
        ('Accion', 'Acción'),
        ('Comedia', 'Comedia'),
        ('Musical', 'Musical'),
    ]

    CLASIFICACION_CHOICES = [
        ('TE', 'TE'),
        ('TE+7', 'TE+7'),
        ('14+', '14+'),
    ]

    sucursal = models.CharField(max_length=100, choices=SUCURSAL_CHOICES)
    nombre = models.CharField(max_length=50, help_text='Nombre de la película')
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES, help_text='Género de la película', blank=False)
    clasificacion = models.CharField(max_length=8, choices=CLASIFICACION_CHOICES, help_text='Clasificación de la película', blank=False)
    duracion = models.PositiveIntegerField(help_text='Tiempo de duración en minutos')
    resena = models.TextField(blank=True, help_text='Breve reseña del contenido de la película')
    sala = models.IntegerField(
        validators=[
            MinValueValidator(1, message="El número de sala debe ser mayor o igual a 1."),
            MaxValueValidator(15, message="El número de sala debe ser menor o igual a 15.")
        ],
        help_text='Sala en la que se exhibe'
    )
    fecha_exhibicion = models.DateField(help_text='Fecha de la exhibición', blank=False)
    hora_exhibicion = models.TimeField(help_text='Hora de la exhibición', blank=False)
    valor_ticket = models.PositiveIntegerField(help_text='Valor del ticket')
    imagen = models.ImageField(upload_to='peliculas/')

    def __str__(self):
        return self.nombre
