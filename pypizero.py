import requests

url = "https://timeapi.io/api/Time/current/zone?timeZone=Europe/Madrid"

response = requests.get(url, timeout=5)
response.raise_for_status()

data = response.json()

print(f"Fecha: {data['date']}")
print(f"Hora: {data['time']}")
print(f"Zona: {data['timeZone']}")