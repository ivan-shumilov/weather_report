from django.contrib import admin
from .models import WeatherCity


class WeatherCityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'degree', 'created')
    search_fields = ('city_name', 'degree')
    save_on_top = True


admin.site.register(WeatherCity, WeatherCityAdmin)
