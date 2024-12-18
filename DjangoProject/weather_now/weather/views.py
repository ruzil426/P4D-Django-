from django.shortcuts import render
import requests
from .forms import CityInput

# Create your views here.
def getter(request):
    data = {}
    if request.method == 'POST':
        form = CityInput(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
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
    else:
        return render(request, 'home.html')
    return render(request, 'basic.html', context=data)


