from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.user.forms import RegistrationForm


class RegistrationView(FormView):
    form_class = RegistrationForm
    success_url = reverse_lazy("admin:index")
    template_name = "user/registration.html"

    def form_valid(self, form: RegistrationForm):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
