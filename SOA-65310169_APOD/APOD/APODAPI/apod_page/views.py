import requests
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def apod_view(request):
    API_URL = "https://api.nasa.gov/planetary/apod"
    # ตรวจสอบวันที่จาก query parameter (ถ้ามี)
    date = request.GET.get('date', '')
    
    params = {
        'api_key': settings.NASA_API_KEY,
    }
    
    if date:
        params['date'] = date

    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return render(request, 'apod_page/apod-app.html', {'data': data})
    else:
         return HttpResponse('Unable to load data at this time.', status=500)

