from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .serializer import SearchHistorySerializer
from .models import SearchHistory, User
import requests
from django.contrib import messages


# Create your views here.
class Search(APIView):
    def get(self, request):
        user_search_history = SearchHistory.objects.filter(user=request.user)
        data = {'user_search_history' : user_search_history, "title": "Weather Application"}
        return render(request, 'home.html', data)


    def post(self, request):
        city_name = request.data['city']
        payload_city = {'apikey':'DjZKAe436auERjukIt9nL1yo1NGaMkde', 'q':city_name, 'language':'en-us', 'details':'false', 'offset':0}
        response = requests.get('http://dataservice.accuweather.com/locations/v1/cities/search', payload_city)
        city_information = response.json()
        location_key = 0

        if len(city_information) != 0:
            for city in city_information:
                location_key = city['Key']

            payload_weather = {'apikey':'DjZKAe436auERjukIt9nL1yo1NGaMkde'}
            api_endpoint = 'http://dataservice.accuweather.com/currentconditions/v1/'+location_key
            weather_data_location = requests.get(api_endpoint, payload_weather)

            serialized_data = {"user":request.user.id, "location":location_key, "weather_data":weather_data_location.json(), "city_name": city_name}

            for weather in weather_data_location.json():
                weather_text = weather["WeatherText"]
                temperature = weather["Temperature"]["Metric"]["Value"]
            serializer = SearchHistorySerializer(data=serialized_data)
            if serializer.is_valid():
                serializer.save()
            data = {"temperature": temperature, "weather_text": weather_text, "city": city_name.title()}
        else:
            messages.error(request, "City not found.")
            data = {"weather_data_location": "Error"}
        return render(request, 'home.html', data)