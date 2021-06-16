import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from .wind import direction


# Парсер
def parsing_weather(request):
    appid = '11111111111111111111111111111111'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    max_count = 5

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()

    if request.method == 'GET':
        max_count = int(request.GET.get('count', 5))

    i = 1
    # Получение таблицы с названиями городов
    cities = City.objects.all()
    if max_count == 0:
        cities.delete()
    all_info = []
    # Парсинг информации с погодой в этих городах
    for city in cities[::-1]:
        if i <= max_count:
            response = requests.get(url.format(city.name)).json()
            if response['cod'] == 200:
                weather_info = {
                    'city': city.name,
                    'temp': response['main']['temp'],
                    'feels_like': response['main']['feels_like'],
                    'pressure': response['main']['pressure'],
                    'wind_speed': response['wind']['speed'],
                    'wind_deg': direction(response),
                    'humidity': response['main']['humidity'],
                    'icon': response['weather'][0]['icon']
                }
                all_info.append(weather_info)
                i += 1
    info = {'all_info': all_info, 'form': form}
    return render(request, 'weather.html', info)
