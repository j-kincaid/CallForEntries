from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def artworks(request):
    page = 'Artworks'
    number = 10
    context = {'page': page, 'number': number}

    return render(request, 'artworks/artworks.html', context)


def artwork(request, pk):
    return render(request, 'artworks/single-artwork.html')
