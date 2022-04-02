
from django.http import Http404
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Panel
# class-based views
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .forms import PanelForm

### Template
class PanelView(TemplateView):
    template_name = 'panel/welcome.html'
    extra_content = {'today': datetime.today()}

### List
class PanelListView(ListView):
    model = Panel
    context_object_name = 'panels'
    template_name = 'panel/panel_list.html'

### Detail 
class PanelDetailView(DetailView):
    model = Panel
    context_object_name = 'panel'

### Create 
class PanelCreateView(CreateView):
    model = Panel
    # fields = ['full_name', 'medium', 'bio']
    success_url = '/panel/new'
    form_class = PanelForm

### Update
class PanelUpdateView(UpdateView):
    model = Panel
    success_url = '/panel/new'
    form_class = PanelForm

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'panel/authorized.html'
    login_url = '/admin'
