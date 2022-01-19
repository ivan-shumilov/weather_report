from django.db import models
from django.utils.translation import gettext_lazy as _


class WeatherCity(models.Model):
    city_name = models.CharField(verbose_name=_('city name'), max_length=255)
    degree = models.FloatField(verbose_name=_('degree'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    class Meta:
        verbose_name_plural = _('weather in cities')
        verbose_name = _('weather in city')
        app_label = 'core'
        ordering = ('city_name',)

    def __str__(self):
        return self.city_name
