import phonenumbers   #for get country name
import opencage #for get location 
import folium # to see location on map
from test import number

from phonenumbers import geocoder    #for get country name
from phonenumbers import carrier     #for get service provider
from opencage.geocoder import OpenCageGeocode   #for get location 

# country name
ch_number=phonenumbers.parse(number,"CH")
location=geocoder.description_for_number(ch_number,"en")


# service provider
service_provider=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_provider,"en"))


# location
key='26d2f0e53d4747b987d900c90a787542'
geocoder=OpenCageGeocode(key)
query=str(location)
result=geocoder.geocode(query)
lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)


# to see location on map
myMap=folium.Map(location=[lat,lng],zoom_start=9)
#arrange the map
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("mylocation.html")