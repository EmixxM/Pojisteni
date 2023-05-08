from django.shortcuts import redirect, render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

from pojisteni.forms import PojistenyForm


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