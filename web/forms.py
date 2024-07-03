from django import forms
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User
from .models import Genero,Registro_cliente

class SignUpForm(UserCreationForm):
    genero      = forms.ModelChoiceField(Genero.objects.all(),required=True,label="Genero")
    fecha_nac   = forms.DateField()
    cel         = forms.IntegerField()
    class Meta:
        model=User
        fields = ['username', 'password1', 'password2', 'email', 'genero', 'fecha_nac','cel']
    pass


