from django.shortcuts import render  # Importar render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Laboratorio
from .forms import LaboratorioForm

def home(request):
    return render(request, 'laboratorio/home.html')

class LaboratorioList(ListView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_list.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Contador de visitas basado en la sesión
        visitas = self.request.session.get('laboratorio_visitas', 0)
        self.request.session['laboratorio_visitas'] = visitas + 1
        context['visitas'] = visitas + 1
        return context


class LaboratorioCreate(CreateView):
    model = Laboratorio
    form_class = LaboratorioForm
    template_name = 'laboratorio/laboratorio_form.html'
    success_url = reverse_lazy('laboratorio:laboratorio_list')

class LaboratorioUpdate(UpdateView):
    model = Laboratorio
    form_class = LaboratorioForm
    template_name = 'laboratorio/laboratorio_form.html'
    success_url = reverse_lazy('laboratorio:laboratorio_list')

class LaboratorioDelete(DeleteView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_confirm_delete.html'
    success_url = reverse_lazy('laboratorio:laboratorio_list')

class LaboratorioDetail(DetailView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_detail.html'
