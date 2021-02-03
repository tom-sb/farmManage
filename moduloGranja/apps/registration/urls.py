from django.urls import path, include
from apps.registration.views import registro

urlpatterns = [
    path('', registro),
]
