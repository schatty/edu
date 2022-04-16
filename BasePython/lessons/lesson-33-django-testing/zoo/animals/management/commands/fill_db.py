from django.core.management.base import BaseCommand

from animals.models import Animal, AnimalKind, AnimalDetail, AnimalFood


class Command(BaseCommand):

    def handle(self, *args, **options):
        foods = ['banana', 'meet', 'water', 'milk']
        for food in foods:
            AnimalFood.objects.get_or_create(name=food)