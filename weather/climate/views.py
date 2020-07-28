import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8e9fa2323ae693217ad94ed7f6647945'
    city = 'Las Vegas'
    r = requests.get(url.format(city)).json()
    # print(r.text)

    city_weather ={
        'city': city,
         'temperature': r['main']['temp'],
         'description':r['weather'][0]['description'],
         'icon':r['weather'][0]['icon'] ,
    }
    context = {'city_weather': city_weather}
    return render (request, 'climate/weather.html', context)