from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    re_path('api/v1/forecast-now', csrf_exempt(views.ForecastNowAPIView.as_view()), name='forecast-now'),
    re_path('', views.home, name='home')
]
