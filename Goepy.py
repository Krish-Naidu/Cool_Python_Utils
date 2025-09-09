from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geo_app")
location = geolocator.geocode("Eiffel Tower")

print(" Address:", location.address)
print(" Coordinates:", (location.latitude, location.longitude))