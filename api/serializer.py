from rest_framework import serializers
from .models import Programmer
class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        # fields = ('fullname','languaje','is_active’) acá podemos traer cualquier atributo del modelo o campo
        fields = '__all__'
        # con la opción de '__all__' nos traemos todo para ver y tener acceso a todo el registro de cada programador

from rest_framework import serializers 
from .models import Tarea 
 
class TareaSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Tarea 
        fields = '__all__' 

from django.shortcuts import render 
from rest_framework import viewsets 
from .serializer import ProgrammerSerializer 
from .models import Programmer 
from rest_framework import viewsets, permissions 
 
# Create your views here. 
 
class ProgrammerViewSet(viewsets.ModelViewSet): 
    # acá creamos una consulta o QUERY a nuestra tabla, trayendo todos los campos como un objeto. 
    queryset = Programmer.objects.all() 
    # Agregamos la clase ProgrammerSerializer que ya tiene el modelo serializado para mostrar 
    serializer_class = ProgrammerSerializer 
    permission_classes = [permissions.IsAuthenticated]  # Requiere JWT