
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
    template_name = "core/ocorrencia_list.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        

        context['total_cadastradas'] = Ocorrencia.objects.count()
        context['total_pendentes'] = Ocorrencia.objects.filter(status='pendente').count()
        

        context['total_andamento'] = Ocorrencia.objects.filter(status='andamento').count()
        context['total_resolvidas'] = Ocorrencia.objects.filter(status='resolvida').count()
        
        context['form'] = OcorrenciaForm()
        return context

    def post(self, request, *args, **kwargs):
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            form.save()
            from django.shortcuts import redirect
            return redirect('core:list') # Redireciona para atualizar os números
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

    