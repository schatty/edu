from django.views.generic import CreateView

from eauth.forms import UserCreateForm
from eauth.models import UserProfile


class UserCreateView(CreateView):
    model = UserProfile
    success_url = "/"  # can be reverse_lazy in future
    form_class = UserCreateForm