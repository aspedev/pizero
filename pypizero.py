import requests
from datetime import datetime

def get_time_from_web():
    url = "http://worldtimeapi.org/api/ip"
    
    response = requests.get(url)
    data = response.json()

    datetime_str = data["datetime"]
    
    # Convertir a formato más legible
    dt = datetime.fromisoformat(datetime_str[:-1])
    
    return dt

if __name__ == "__main__":
    print("Consultando hora desde Internet...\n")
    
    now = get_time_from_web()
    
    print("Hora actual:")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))