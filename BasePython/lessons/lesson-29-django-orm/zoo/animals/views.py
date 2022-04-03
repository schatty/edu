from django.shortcuts import render

from .models import Animal


def index(request):
    # all_animals = Animal.objects.all()
    # all_animals = Animal.objects.select_related('kind').all()
    all_animals = Animal.objects.prefetch_related('animalfood_set').all()
    print("All animals:", all_animals)
    context = {
        "all_animals": all_animals
    }

    return render(request, 'index.html', context=context)