from django.http import Http404
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Panel
# class-based views
from django.views.generic import TemplateView, ListView, DetailView

class PanelDetailView(DetailView):
    model = Panel
    context_object_name = 'panel'

class PanelListView(ListView):
    model = Panel
    context_object_name = 'panels'
    template_name = 'panel/panel_list.html'

class PanelView(TemplateView):
    template_name = 'panel/welcome.html'
    extra_content = {'today': datetime.today()}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'panel/authorized.html'
    login_url = '/admin'

def detail(request, pk):
    try:
        panel = Panel.objects.get(pk=pk)
    except Panel.DoesNotExist:
        raise Http404("Panelist doesn't exist")
    return render(request, 'panel/panel_list.html', {'panel': panel})