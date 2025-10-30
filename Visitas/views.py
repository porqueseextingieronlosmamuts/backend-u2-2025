from django.shortcuts import render, get_object_or_404, redirect
from .models import Visita
from django.utils import timezone
from .forms import VisitaForm

def lista_visitas(request):
    hoy = timezone.now().date()
    visitas = Visita.objects.filter(hora_de_entrada_y_salida__date=hoy)
    return render(request, 'visitas/lista_visitas.html', {'visitas': visitas})

def detalle_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    return render(request, 'visitas/detalle_visita.html', {'visita': visita})

def nueva_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = VisitaForm()
    return render(request, 'visitas/nueva_visita.html', {'form': form})

def editar_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    if request.method == 'POST':
        form = VisitaForm(request.POST, instance=visita)
        if form.is_valid():
            form.save()
            return redirect('detalle_visita', id=visita.id)
    else:
        form = VisitaForm(instance=visita)
    return render(request, 'Visitas/editar_visita.html', {'form': form})

def eliminar_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    if request.method == 'POST':
        visita.delete()
        return redirect('lista_visitas')
    return render(request, 'visitas/eliminar_visita.html', {'visita': visita})

