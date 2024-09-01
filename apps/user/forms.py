from django import forms

from apps.user.models import Subscriber


class SubscriberForm(forms.Form):
    email = forms.EmailField(
        label='',
        max_length=254,
        widget=forms.EmailInput(
            attrs={'placeholder': 'Enter your email address'}
        )
    )

    def create_subscriber(self) -> Subscriber:
        email = self.cleaned_data['email']
        subscriber, _ = Subscriber.objects.get_or_create(email=email)
        return subscriber
