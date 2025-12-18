from django.shortcuts import render
from .models import Visit
 
def index(request):
    # Zapis każdej wizyty
    Visit.objects.create()
    # Pobranie liczby wszystkich wizyt
    visits = Visit.objects.count()
    # Przekazanie liczby wizyt do szablonu
    return render(request, "index.html", {"visits": visits})