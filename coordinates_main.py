from gmaps import Geocoding
api = Geocoding(api_key='AIzaSyBGJgF7gltKbGbyEdio03s5vmYoIc6Uww8')
geofind=api.geocode(input('Enter location: '))
geofind[0]
print(geofind[0]['geometry']['location'])
