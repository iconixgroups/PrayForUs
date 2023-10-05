```python
import requests
from src.user_profile import userDetails
from src.church_listings import churchDetails

# Google Maps API Key
API_KEY = "YOUR_API_KEY"

def get_location(address):
    """
    Function to get latitude and longitude of a given address using Google Maps API
    """
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'OK':
        latitude = data['results'][0]['geometry']['location']['lat']
        longitude = data['results'][0]['geometry']['location']['lng']
        return latitude, longitude
    else:
        return None, None

def display_church_locations():
    """
    Function to display church locations on a map
    """
    for church in churchDetails:
        address = church['address']
        latitude, longitude = get_location(address)
        if latitude and longitude:
            # Display the location on the map
            pass  # Implementation depends on the front-end library used

def search_church_by_location(location):
    """
    Function to enable proximity searches for churches
    """
    user_latitude, user_longitude = get_location(location)
    if user_latitude and user_longitude:
        for church in churchDetails:
            church_latitude, church_longitude = get_location(church['address'])
            distance = calculate_distance(user_latitude, user_longitude, church_latitude, church_longitude)
            if distance <= 10:  # Assuming the distance is in kilometers
                # Display the church in the search results
                pass  # Implementation depends on the front-end library used

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Function to calculate the distance between two points on the earth specified by latitude and longitude
    """
    from math import sin, cos, sqrt, atan2, radians

    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance
```