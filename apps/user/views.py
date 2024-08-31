from django.http import JsonResponse
from django.views.generic import View
from django.utils.translation import gettext_lazy as _

from apps.user.forms import SubscriberForm


class SubscribeView(View):

    def post(self, *args, **kwargs) -> JsonResponse:
        form = SubscriberForm(self.request.POST)
        if not form.is_valid():
            return JsonResponse({'errors': form.errors}, status=400)

        try:
            form.create_subscriber()
        except Exception:
            return JsonResponse(
                data={'message': _('Internal server error')},
                status=500
            )

        return JsonResponse(
            data={'message': _('Successfully subscribed')},
            status=200
        )
