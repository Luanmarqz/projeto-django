
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ocorrencia
from django.views.generic import ListView
from .models import Ocorrencia
from .forms import OcorrenciaForm

class OcorrenciaView(ListView):
    model = Ocorrencia
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OcorrenciaForm()
        return context

    def post(self, request, *args, **kwargs):
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request, *args, **kwargs)
class OcorrenciaCreateView(CreateView):
    model = Ocorrencia
    fields = '__all__'
    success_url = reverse_lazy('core:list')

class OcorrenciaUpdateView(UpdateView):
    model = Ocorrencia
    form_class = OcorrenciaForm
    template_name = "core/includes/modais_conteudo.html" # Aponta para o arquivo único
    success_url = reverse_lazy('core:list')

class OcorrenciaDetailView(DetailView):
    model = Ocorrencia
    template_name = "core/includes/modais_conteudo.html" # Aponta para o arquivo único

class OcorrenciaDeleteView(DeleteView):
    model = Ocorrencia
    template_name = "core/includes/modais_conteudo.html" # Aponta para o arquivo único
    success_url = reverse_lazy('core:list')