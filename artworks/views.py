from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def artworks(request):
    return HttpResponse('Here are the artworks')


def artwork(request, pk):
    return HttpResponse('Single artwork' + ' ' + str(pk))

