import urllib.request
import json
from django.shortcuts import render


def Weather(request):

    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=da4d53923110285a905ac164e58f2765').read()
        list_of_data = json.loads(source)

        data = {
            "temp": str(list_of_data['main']['temp']),
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
        }
        print(data)
    else:
        data = {}

    return render(request, "home.html", data)

