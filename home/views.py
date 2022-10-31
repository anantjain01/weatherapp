
from datetime import datetime
from decimal import FloatOperation
from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    city = request.GET.get('city',"kota")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=fbccb8b7188ab87c7a0d619c8bb2defd'
    data = requests.get(url).json()
    # print(data)
    payload = { 
        'city':data['name'],
        'weather':data['weather'][0]['main'],
        'icon':data['weather'][0]['icon'],
        'temperature':int(data['main']['temp']-273),
        'feel':int(data['main']['feels_like']-273),
        'temp_min':float(data['main']['temp_min']-273),
        'temp_max':float(data['main']['temp_max']-273),
        'time': datetime.today()
    }
    context={'data':payload}
    print(context)
    return render(request,'home.html',context)

