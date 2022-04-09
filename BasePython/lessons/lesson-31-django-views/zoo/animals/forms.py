from django.forms import ModelForm

from animals.models import Animal


class AnimalCreateForm(ModelForm):
    class Meta:
        model = Animal
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, widget in self.fields.items():
            print(name)
            print(widget)