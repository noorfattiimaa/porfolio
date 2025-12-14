from django.urls import path
from .views import index, thank_you

urlpatterns = [
    path('', index, name='home'),
    path('thank-you/', thank_you, name='thank_you'),
]
