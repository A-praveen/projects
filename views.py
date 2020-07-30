import requests
from django.core.files import temp
from django.shortcuts import render

# Create your views here.
def weather(request):
    url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=1f243de9c538872686ae7e449aec6765"
    city='bangalore'
    r=requests.get(url.format(city)).json()
    city_weather={
        'city' : city,
        'temperature' : int (r['main']['temp']-273.15),
        'description' : r['weather'][0]['description'],

    }


    return render(request, "weather.html", {'city_weather': city_weather})


