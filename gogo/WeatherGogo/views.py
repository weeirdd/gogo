from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from django.shortcuts import render
import sqlite3


def index(request):
    appid = 'df1a063efe9704a0693d95fc88b6c922'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []
    for city in cities:
        response = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': response["main"]["temp"],
            'icon': response["weather"][0]["icon"],
            'feels': response["main"]["feels_like"]
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)


def weekweather(request):
    return render(request, 'weather/weekweather.html')

def outfits(request):
    print(66)
    db = sqlite3.connect('gogo_db')
    c = db.cursor()
    select_query = "SELECT * FROM outfit"
    c.execute(select_query)
    result = c.fetchall()
    db.commit()
    db.close()

    all_images = []
    print(result)

    # for city in cities:
    #     city_info = {
    #         'city': city.name,
    #         'temp': response["main"]["temp"],
    #         'icon': response["weather"][0]["icon"],
    #         'feels': response["main"]["feels_like"]
    #     }
    #     all_cities.append(city_info)
    #
    # context = {'all_info': all_images}

    return render(request, 'weather/outfits.html')

def register(request):
    return render(request, 'weather/register.html')

def support(request):
    return render(request, 'weather/support.html')

def feedback(request):
    return render(request, 'weather/feedback.html')