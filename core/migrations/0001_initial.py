# Generated by Django 4.0.1 on 2022-01-19 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=255, verbose_name='city name')),
                ('degree', models.FloatField(verbose_name='degree')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
            options={
                'verbose_name': 'weather in city',
                'verbose_name_plural': 'weather in cities',
                'ordering': ('city_name',),
            },
        ),
    ]