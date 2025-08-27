from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render <-- esta libreria no la usamos por ahora
from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .serializer import TareaSerializer
from .models import Programmer, Tarea, Proyecto
from rest_framework import permissions

from django.contrib.auth.models import User

# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere JWT

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProgrammerSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere JWT

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere JWT

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere JWT



def home(request):
    return render(request, "home.html")

