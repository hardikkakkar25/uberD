# urls.py
from django.urls import path
from pricing.views import CalculatePriceAPI


urlpatterns = [
    path('api/calculate-price/', CalculatePriceAPI.as_view(), name='calculate-price'),
]
