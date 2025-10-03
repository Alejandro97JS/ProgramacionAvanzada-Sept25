# Script para consultar la API de Open-Meteo para Madrid
import requests

# Coordenadas de Madrid
LAT = 40.4168
LON = -3.7038
URL = (
	f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}"
	"&hourly=temperature_2m,relative_humidity_2m,windspeed_10m"
	"&current_weather=true"
	"&timezone=Europe%2FMadrid"
)


def _print_current_weather_from_current(data: dict) -> bool:
	"""Try to print `current_weather` block. Return True if printed."""
	weather = data.get("current_weather")
	if not weather:
		return False

	print("Clima actual en Madrid (current_weather):")
	print(f"Temperatura: {weather.get('temperature', 'N/A')}°C")
	print(f"Viento: {weather.get('windspeed', 'N/A')} km/h")
	print(f"Dirección del viento: {weather.get('winddirection', 'N/A')}°")
	print(f"Condición (weathercode): {weather.get('weathercode', 'N/A')}")
	return True


def _print_current_weather_from_hourly(data: dict) -> bool:
	"""Fallback: use the latest timestamp from hourly data if current_weather missing."""
	hourly = data.get("hourly") or {}
	times = hourly.get("time") or []
	if not times:
		return False

	idx = len(times) - 1
	time = times[idx]
	temp_list = hourly.get("temperature_2m", [])
	ws_list = hourly.get("windspeed_10m", [])
	rh_list = hourly.get("relative_humidity_2m", [])

	# Safe access
	temp = temp_list[idx] if idx < len(temp_list) else "N/A"
	ws = ws_list[idx] if idx < len(ws_list) else "N/A"
	rh = rh_list[idx] if idx < len(rh_list) else "N/A"

	print(f"Clima en Madrid para {time} (último dato hourly):")
	print(f"Temperatura: {temp}°C")
	print(f"Viento: {ws} km/h")
	print(f"Humedad relativa: {rh}%")
	return True


def main():
	try:
		response = requests.get(URL, timeout=10)
	except requests.RequestException as exc:
		print(f"Error al realizar la petición: {exc}")
		return

	if response.status_code != 200:
		print(f"Error al obtener datos: {response.status_code}")
		print(response.text)
		return

	data = response.json()

	# Try current_weather first, then fallback to hourly
	if _print_current_weather_from_current(data):
		return

	if _print_current_weather_from_hourly(data):
		return

	print("No se han encontrado datos de clima en la respuesta.")


if __name__ == "__main__":
	main()
