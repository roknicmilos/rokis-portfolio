from apps.user.views import SubscribeFormView


class IndexView(SubscribeFormView):
    template_name = 'index.html'
