from django import forms
from django.contrib.auth.forms import BaseUserCreationForm

from apps.portfolio import service as portfolio_service

from apps.user.models import Subscriber, User


class SubscriberForm(forms.Form):
    email = forms.EmailField(
        label="",
        max_length=254,
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter your email address"}
        ),
    )

    def create_subscriber(self) -> Subscriber:
        email = self.cleaned_data["email"]
        subscriber, is_created = Subscriber.objects.get_or_create(email=email)
        if not is_created:
            subscriber.update(submission_count=subscriber.submission_count + 1)

        return subscriber


class RegistrationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ("email",)

    def save(self, commit=True) -> User:
        self.instance.is_active = True
        self.instance.is_staff = True
        user = self.set_password_and_save(self.instance)
        user.user_permissions.add(
            *portfolio_service.get_default_portfolio_permission()
        )
        return user
