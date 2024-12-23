from django.shortcuts import render
import requests
from .forms import CityInput
from .models import City
from django.http import HttpResponseRedirect

# Create your views here.
def getter(request):
    data = {}
    if request.method == 'POST':
        form = CityInput(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            city_data = City()
            url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
            weather_data = requests.get(url).json()
            data = {
                'city': city,
                'temperature': round(weather_data['main']['temp'], 1),
                'temperature_feels': round(weather_data['main']['feels_like'], 1),
                'humidity': weather_data['main']['humidity'],
                'visibility': weather_data['visibility']/1000,
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon'],
            }
            city_data.name = city
            city_data.temperature = round(weather_data['main']['temp'], 1)
            city_data.temperature_feels = round(weather_data['main']['feels_like'], 1)
            city_data.humidity = weather_data['main']['humidity']
            city_data.visibility = weather_data['visibility']/1000
            city_data.description = weather_data['weather'][0]['description']
            city_data.icon = weather_data['weather'][0]['icon']
            city_data.save()
    else:
        return render(request, 'home.html')
    city_info = City.objects.all()
    return render(request, 'basic.html', context={"data": data, "city_info": city_info})

def delete(request, city_id):
    if request.method == 'GET':
        city_data = City.objects.filter(id=city_id)
        city_data.delete()
        return HttpResponseRedirect("/")

def delete_all(request):
    if request.method == 'GET':
        city_data = City.objects.all()
        city_data.delete()
        return HttpResponseRedirect("/")


