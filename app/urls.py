from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('puberdade/', views.topicos, name='puberdade'),
    path('topicos/', views.topicos, name='topicos'),
]