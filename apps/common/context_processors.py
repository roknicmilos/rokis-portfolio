from django.conf import settings


def settings_variables(request):
    return {
        "GOOGLE_ANALYTICS_TRACKING_ID": settings.GOOGLE_ANALYTICS_TRACKING_ID,
    }
