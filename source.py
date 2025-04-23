import phonenumbers
from phonenumbers import geocoder
import folium
key = "b4873bf6c4c0423c8dffa2ea09f7f52e"

number = input("enter the ph.no with country code:")
check_number = phonenumbers.parse(number)
location = geocoder.description_for_number(check_number,"en")
print(location)

from phonenumbers import carrier
sim = phonenumbers.parse(number)
print(carrier.name_for_number(sim,"en"))

from opencage.geocoder import OpenCageGeocode
geocode = OpenCageGeocode(key)

query = str(location)
results = geocode.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

map_location = folium.Map(location = [lat,lng],zoom_start=10)
folium.Marker([lat,lng],popup=location).add_to(map_location)
map_location.save("loc.html")

