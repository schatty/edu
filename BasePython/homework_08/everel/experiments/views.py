from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Run


def index(request):
    context = {
    }

    return render(request, 'experiments/index.html', context=context)


class BrowseView(ListView):
    model = Run
    success_url = reverse_lazy('browse')
    paginate_by = 10


class RunDetailView(DetailView):
    template_name = 'experiments/run.html'
    model = Run
    context_object_name = "run"
    pk_url_kwarg = 'id'