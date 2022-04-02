from django.shortcuts import render

from .models import Animal


def index(request):
    all_animals = Animal.objects.all()
    print("All animals:", all_animals)
    context = {
        "all_animals": all_animals
    }

    return render(request, 'index.html', context=context)