from django.urls import path, include

from .views import index, htmx_home, htmx_updated

urlpatterns = [
    path('', index, name='index-page'),
    path('htmx-home/', htmx_home, name='htmx-home'),
    path('htmx-updated/', htmx_updated, name='htmx-updated'),
]
