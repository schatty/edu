from django.contrib.auth.forms import UserCreationForm

from eauth.models import UserProfile


class UserCreateForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2')