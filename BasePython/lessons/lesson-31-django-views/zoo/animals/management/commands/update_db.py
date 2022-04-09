from django.core.management.base import BaseCommand

from animals.models import Animal, AnimalKind, AnimalDetail


class Command(BaseCommand):

    def handle(self, *args, **options):
        to_update_animals = Animal.objects.filter(animaldetail__isnull=True)
        for animal in to_update_animals:
            AnimalDetail.objects.create(
                animal=animal,
                biography="to be filled"
            )
            print(f"for {animal} detail created")