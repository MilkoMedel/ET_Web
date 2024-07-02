# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/',views.nosotros,name='nosotros'),
    path('galeria/',views.galeria,name='galeria'),
    path('login/',views.login,name='login'),
    path('form/',views.form,name='form'),
]

