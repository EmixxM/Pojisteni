from django.shortcuts import redirect, render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

from pojisteni.forms import PojistenyForm
from pojisteni.forms import PojisteniForm


from .models import Pojisteny

def seznam_pojistenych(request):
    pojisteni = Pojisteny.objects.all()
    return render(request, 'seznam_pojistenych.html', {'pojisteni': pojisteni})

def detail_pojisteneho(request, pk):
    pojisteny = get_object_or_404(Pojisteny, pk=pk)
    return render(request, 'detail_pojisteneho.html', {'pojisteny': pojisteny})


def novy_pojisteny(request):
    if request.method == 'POST':
        # Zpracování formuláře pro přidání nového pojištěnce
        form = PojistenyForm(request.POST)
        if form.is_valid():
            form.save()
            # Přesměrování na seznam pojištěných po uložení
            return redirect('seznam_pojistenych')
    else:
        # Zobrazení prázdného formuláře pro přidání nového pojištěnce
        form = PojistenyForm()

    return render(request, 'novy_pojisteny.html', {'form': form})


def pridat_pojisteni(request):
    if request.method == 'POST':
        # Zpracování formuláře pro přidání nového pojištění
        form = PojisteniForm(request.POST)
        if form.is_valid():
            form.save()
            # Přesměrování na detail nově přidaného pojištění
            return redirect('detail_pojisteneho', pk=form.instance.pk)
    else:
        # Zobrazení prázdného formuláře pro přidání nového pojištění
        form = PojisteniForm()

    return render(request, 'pridat_pojisteni.html', {'form': form})


def editovat_pojisteneho(request, pk):
    pojisteny = get_object_or_404(Pojisteny, pk=pk)

    if request.method == 'POST':
        form = PojistenyForm(request.POST, instance=pojisteny)
        if form.is_valid():
            form.save()
            return redirect('detail_pojisteneho', pk=pojisteny.pk)
    else:
        form = PojistenyForm(instance=pojisteny)

    return render(request, 'editovat_pojisteneho.html', {'form': form, 'pojisteny': pojisteny})

def odstranit_pojisteneho(request, pk):
    pojisteny = get_object_or_404(Pojisteny, pk=pk)

    if request.method == 'POST':
        pojisteny.delete()
        return redirect('seznam_pojistenych')

    return render(request, 'odstranit_pojisteneho.html', {'pojisteny': pojisteny})
