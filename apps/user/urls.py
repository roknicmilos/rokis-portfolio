from django.urls import path
from apps.user.views import SubscribeView

app_name = 'user'
urlpatterns = [
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
]
