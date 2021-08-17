from mapbox import Geocoder
import json
import requests
mb_API_Key = "pk.eyJ1IjoidGhlY29vbGVyamFtcyIsImEiOiJja2x2N3I0bWcwNm5uMm9xb2YycTRrZmp6In0.HeT7Nh005EmxAxq47waiPw"
def get_route(source, destination):
        coordinate_string = f"{source['longitude']},{source['latitude']};" \
                            f"{destination['longitude']},{destination['latitude']}"

        mapbox_url = "https://api.mapbox.com/directions/v5/mapbox/driving/" + coordinate_string + ".json"
        params = {"access_token": mb_API_Key}

        # combine the above data into a mapbox route request
        response = requests.get(mapbox_url, params=params)
        mapbox_route = response.json()

        return mapbox_route

def get_coordinates_of_destination(destination_address):
        mapbox_url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + destination_address + ".json"
        params = {"limit": 1, "access_token": mb_API_Key}

        # combine the above data into a mapbox forward geocoding request
        response = requests.get(mapbox_url, params=params)
        mapbox_geo = response.json()

        # destination is a list of the coordinates
        destination = mapbox_geo['features'][0]['geometry']['coordinates']
        destination_dict = {'latitude': destination[1], 'longitude': destination[0]}

        return destination_dict

def geteta():
    pass


def display_address_of_coor(coor_lat, coor_long):
    mapbox_url = "https://api.mapbox.com/geocoding/v5/mapbox.places/"
    geocodingRequest = requests.get(
        mapbox_url + str(coor_lat) + "," + str(coor_long) + ".json?access_token=" + mb_API_Key)
    map_data = geocodingRequest.json()
    address = json.dumps(map_data.get("features")[0].get('place_name'))
    return address

print(display_address_of_coor(-97.7526,30.2289))
start_address = get_coordinates_of_destination("423 Chancellorsville Drive, Mesquite, TX75149")
end_address = get_coordinates_of_destination("1111 E Davis St, Mesquite, TX 75149")
print(get_route(start_address,end_address))