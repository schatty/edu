from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from .forms import AnimalCreateForm
from .models import Animal

# @login_required
def index(request):
    # all_animals = Animal.objects.all()
    # all_animals = Animal.objects.select_related('kind').all()
    all_animals = Animal.objects.prefetch_related('animalfood_set').all()
    print("All animals:", all_animals)
    context = {
        "all_animals": all_animals
    }

    return render(request, 'animals/index.html', context=context)


def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    context = {
        "animal": animal
    }
    return render(request, "animals/animal.html", context)


class PageTitleMixin:
    page_title = ''

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Animal Detail"
        return context


class AnimalDetailView(PageTitleMixin, DetailView):
    template_name = 'animals/animal.html'
    model = Animal
    pk_url_kwarg = 'pk'
    context_object_name = 'animal'
    page_title = "Animal Detail"


class AnimalCreateView(LoginRequiredMixin, CreateView):
   model = Animal
   success_url = reverse_lazy('main')
   form_class = AnimalCreateForm
#    fields = "__all__" 


class AnimalUpdateView(UpdateView):
   model = Animal
   success_url = reverse_lazy('main')
   fields = "__all__" 


