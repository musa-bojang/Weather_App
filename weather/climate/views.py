import requests
from django.shortcuts import render
from .models import City
# Create your views here.
def index(request):
    # change units=imperial to units=metric
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=8e9fa2323ae693217ad94ed7f6647945'
    city = 'Nilai'
    cities = City.objects.all()
    # print(r.text)
    weather_data =[]
    
    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'] ,
        }
        weather_data.append(city_weather)
    # print(weather_data)
    context = {'weather_data': weather_data}
    return render (request, 'climate/weather.html', context)