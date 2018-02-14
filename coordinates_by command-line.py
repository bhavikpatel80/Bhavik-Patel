#use python_gmaps module
#Many online providers such as Google & Bing have geocoding services
#Here is a code to get a Lat & Lng from Google
import sys
from gmaps import Geocoding


#create api_key using => https://developers.google.com/maps/documentation/geocoding/start
#api = Geocoding(api_key='Your API_KEY')


api = Geocoding(api_key='AIzaSyBGJgF7gltKbGbyEdio03s5vmYoIc6Uww8')

#find entered loctaion using api geocode
geofind=api.geocode(sys.argv[1])
geofind[0]
print(geofind[0]['geometry']['location'])


