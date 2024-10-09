from django.urls import path

from apps.user.views import RegistrationView

app_name = "user"

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
]
