import json
import socket
import arrow
import requests
from django.conf import settings
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework import views, status
from django.shortcuts import render
from .models import WeatherCity


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return None


class ForecastNowAPIView(views.APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = []

    def post(self, request, *args, **kwargs):

        # нужно узнать наименование города и координаты (широта и долгота)
        url = f'{settings.API_IPSTACK_URL}/{socket.gethostbyname(socket.gethostname())}?' \
              f'access_key={settings.API_IPSTACK_KEY}'
        js = json.load(request.urlopen(url))

        latitude = js['latitude']
        longitude = js['longitude']
        city_name = js['city']

        # получаем какая темпиратура в текущий момент времени у указанного города
        start = arrow.now()
        end = arrow.now()
        response = requests.get(
            settings.API_STORMGLASS_URL,
            params={
                'lat': latitude,
                'lng': longitude,
                'params': ','.join(['waveHeight', 'airTemperature']),
                'start': start.to('UTC+3').timestamp(),
                'end': end.to('UTC+3').timestamp()
            },
            headers={
                'Authorization': settings.API_STORMGLASS_KEY
            }
        )
        try:
            # получаем сколько градусов в городе и записываем в базу
            degree = response.json()['hours'][0]['airTemperature']['noaa']
            WeatherCity.objects.create(city_name=city_name, degree=degree)
            return Response({'degree': degree, 'city_name': city_name}, status=status.HTTP_201_CREATED)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


def home(request):
    return render(request, 'layout.html', dict())
