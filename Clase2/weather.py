import requests
from pprint import pprint

class WeatherAPI:
    base_url = "https://api.open-meteo.com/v1/forecast"
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.hourly = "hourly"

    def request_data(self, query_params):
        url = f"{self.base_url}?latitude={self.latitude}&longitude={self.longitude}&"
        request_url = f"{url}{query_params}"
        response = requests.get(request_url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            self.data = None

    def print_data(self, address):
        print(f"Historial de Temperaturas para {address}")
        print("------------------------------------")
        data = weather.data
        horas = data["hourly"]["time"]
        temperaturas = data["hourly"]["temperature_2m"]
        for hora, temp in zip(horas, temperaturas):
            print(f"{hora} → {temp} °C")


class LocationAPI:
    base_url = "https://nominatim.openstreetmap.org/search"

    def get_coordinates(self, location_name):
        params = {
            "q": location_name,
            "format": "json",
            "limit": 1,
            "addressdetails": 1,
            "accept-language": "es"
        }
        headers = {
            "User-Agent": "(feersantana5@gmail.com)"
        }
        response = requests.get(self.base_url, params=params, headers=headers)
        if response.status_code == 200:

            data = response.json()
            if data:
                return {'longitude': data[0]["lon"], 'latitude': data[0]["lat"] }
            else:
                print("No se encontraron resultados")
                return None
        else:
            print("Error:", response.status_code, response.text)
            return None


if __name__ == "__main__":

    address = "Cádiz, España"
    location = LocationAPI()
    coordinates = location.get_coordinates(address)
    weather = WeatherAPI(coordinates.get('latitude'), coordinates.get('longitude'))
    weather.request_data("&hourly=temperature_2m&current=temperature_2m,precipitation,rain,relative_humidity_2m,apparent_temperature,is_day")
    #print(weather.data)
    weather.print_data(address)