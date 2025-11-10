from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import GroupSerializer, UserSerializer,VistaSerializer
from .models import Visita
from django.utils import timezone
from .forms import VisitaForm

class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all().order_by("nombre")
    serializer_class = VistaSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def lista_visitas(request):
    hoy = timezone.now().date()
    visitas = Visita.objects.filter(hora_de_entrada_y_salida__date=hoy)
    return render(request, 'lista_visitas.html', {'visitas': visitas})

def detalle_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    return render(request, 'detalle_visita.html', {'visita': visita})

def nueva_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = VisitaForm()
    return render(request, 'nueva_visita.html', {'form': form})

def editar_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    if request.method == 'POST':
        form = VisitaForm(request.POST, instance=visita)
        if form.is_valid():
            form.save()
            return redirect('detalle_visita', id=visita.id)
    else:
        form = VisitaForm(instance=visita)
    return render(request, 'editar_visita.html', {'form': form})

def eliminar_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    if request.method == 'POST':
        visita.delete()
        return redirect('lista_visitas')
    return render(request, 'eliminar_visita.html', {'visita': visita})

