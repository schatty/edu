from django.contrib import admin

from .models import Animal, AnimalDetail, AnimalKind, AnimalFood

admin.site.register(Animal)
admin.site.register(AnimalDetail)
admin.site.register(AnimalKind)
admin.site.register(AnimalFood)