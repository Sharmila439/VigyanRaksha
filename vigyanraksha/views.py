from django.shortcuts import render,redirect
from django.http import JsonResponse
import requests
import random

    
N2YO_API_KEY  = '7YZH9G-KBAWFK-FDWYVA-5HC5'
def satellite_api(request):
     # Coordinates centered over India
    lat, lon, alt = 20.5937, 78.9629, 0  # Altitude in meters
    radius = 1000  # Radius in kilometers
    category = 0  # 0 for all categories

    url = f"https://api.n2yo.com/rest/v1/satellite/above/{lat}/{lon}/{alt}/{radius}/{category}/&apiKey={N2YO_API_KEY}"

    response = requests.get(url)
    data = response.json()

    results = []
    for sat in data.get("above", []):
        results.append({
            "id": sat.get("satid"),
            "name": sat.get("satname"),
            "latitude": sat.get("satlat"),
            "longitude": sat.get("satlng"),
            "category": classify_category(sat.get("satname"))
        })

    return JsonResponse(results, safe=False)

def classify_category(name):
    name = name.lower()
    if "nav" in name:
        return "Navigation"
    elif "met" in name or "weather" in name:
        return "Weather"
    elif "def" in name or "spy" in name or "gsat" in name:
        return "Defense"
    else:
        return "Other"
    

def satellite_map(request):
    return render(request, 'core/satellite_map.html')

def get_drones(request):
    drones = []
    for i in range(10):  # 10 drones
        drones.append({
            "id": i,
            "name": f"Drone-{i+1}",
            "latitude": round(20 + random.uniform(-5, 5), 5),
            "longitude": round(78 + random.uniform(-5, 5), 5),
            "status": random.choice(["Surveillance", "Standby", "Alert"])
        })
    return JsonResponse(drones, safe=False)

def drone_map(request):
    return render(request, 'core/drone_map.html')

def dashboard(request):
    return render(request, 'core/dashboard.html')

def home(request):
    return render(request, 'core/home.html')
