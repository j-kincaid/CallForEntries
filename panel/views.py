from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

def panel(request):
    return render(request, 'panel/welcome.html', {'today': datetime.today()})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'panel/authorized.html', {})
