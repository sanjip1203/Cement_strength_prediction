from django.urls import path
from .views import predict_csMPa

urlpatterns = [
    path('predict/', predict_csMPa, name='predict_csMPa'),
]
