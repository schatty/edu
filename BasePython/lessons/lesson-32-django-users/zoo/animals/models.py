from pyexpat import model
from django.db import models


class AnimalKind(models.Model):
    name = models.CharField(max_length=32)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField(null=True)
    kind = models.ForeignKey(AnimalKind, on_delete=models.CASCADE, null=True)
    desc = models.TextField(blank=True)

    def __str__(self):
        # return f"Animal: {self.name} ({self.kind}) (eats {self.get_food()})"
        return f"Animal: {self.name} (eats {self.get_food()})"

    def get_food(self):
        # lowercase + suffix set
        food = self.animalfood_set.all()
        return ', '.join(map(str, food))


class AnimalDetail(models.Model):
    animal = models.OneToOneField('animals.Animal',  # name of the application . name of the class
                                  primary_key=True,  # will use primary from from Animal
                                  on_delete=models.CASCADE)
    biography = models.TextField()

    def __str__(self):
        return self.biography


class AnimalFood(models.Model):
    name = models.CharField(max_length=64, unique=True)
    animal = models.ManyToManyField(Animal)

    def __str__(self):
        return self.name