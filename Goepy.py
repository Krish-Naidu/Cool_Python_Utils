geolocator = Nominatim(user_agent="geo_app")
from geopy.geocoders import Nominatim

location_name = input("Enter a location to geocode: ")
geolocator = Nominatim(user_agent="geo_app")
location = geolocator.geocode(location_name)

if location:
	print(" Address:", location.address)
	print(" Coordinates:", (location.latitude, location.longitude))
else:
	print("Location not found")
