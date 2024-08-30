from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index3),
    path('saludo/', views.presentacion_3),
]