from django.urls import path, include

from .views import index, htmx_home, htmx_updated, check_guess

urlpatterns = [
    path('', index, name='index-page'),
    path('htmx-home/', htmx_home, name='htmx-home'),
    path('htmx-updated/', htmx_updated, name='htmx-updated'),
    path("check-guess/", check_guess, name="check-guess"),  # New route for "Enter" button
]
