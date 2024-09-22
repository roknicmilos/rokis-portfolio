from django.views.generic import FormView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from apps.user.forms import SubscriberForm


class SubscribeFormView(FormView):
    form_class = SubscriberForm
    success_url = "."

    def form_valid(self, form: SubscriberForm):
        try:
            form.create_subscriber()
        except Exception:
            messages.error(self.request, _("Internal server error! 🤕"))
        else:
            messages.success(self.request, _("Successfully subscribed! 🥳"))

        return super().form_valid(form)

    def form_invalid(self, form: SubscriberForm):
        messages.error(self.request, _("Invalid email address! 😬"))
        return super().form_invalid(form)
