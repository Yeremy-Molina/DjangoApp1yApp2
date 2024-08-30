from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index_2),
    path('saludo/', views.presentacion_2),
]