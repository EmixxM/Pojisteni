from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse


from .models import Pojisteny

def seznam_pojistenych(request):
    pojisteni = Pojisteny.objects.all()
    return render(request, 'seznam_pojistenych.html', {'pojisteni': pojisteni})

def detail_pojisteneho(request, pk):
    pojisteny = get_object_or_404(Pojisteny, pk=pk)
    return render(request, 'detail_pojisteneho.html', {'pojisteny': pojisteny})