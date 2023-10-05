from django.urls import path, include
from .views import inicio, peliculas

urlpatterns = [
    path('', inicio, name="inicio"),
    path('peliculas/', peliculas, name="peliculas"),
    
]