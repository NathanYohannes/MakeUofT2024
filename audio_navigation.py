from googlemaps import Client
from haversine import haversine, Unit
import pprint
import re
import socket as soc
import json
import os
def main():
    port = 12345
    s = soc.socket()
    s.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR, 1) 
    s.bind(('', port))
    s.listen(1)
    c,addr = s.accept()
    mapService = Client(key='')
    threshold = 1 #distance in meters away from next checkpoint you can be
    gps_location = c.recv(2048).decode('ascii')

    StartDestination = "55 st george st toronto ontario" #input("Start?\n")

    EndDestination = "2222 ellesmere rd" #input("End?\n")

    directions = mapService.directions( StartDestination , EndDestination, mode="walking")
    directions = directions[0]
    #pprint.pprint (directions)

    i=1
    for leg in directions['legs']:
        startAddress = leg['start_address']
        print ("Start Address:", startAddress)
        endAddress = leg['end_address']
        print ("End Address:", endAddress)
        gps_location = c.recv(2048).decode('ascii')
        for step in leg['steps']:
            html_instructions = step['html_instructions']
            end_location = step['end_location']
            clean_instructions = re.compile('<.*?>')
            destination_coords = (end_location["lat"], end_location["lng"])
            
            gps_coords = gps_location_to_tuple(gps_location)
            print("gps coords {}".format(gps_coords))
            print("dest coords {} \n".format(destination_coords))
             
            distance = get_coords_distance_meters(gps_coords, destination_coords)
            print("{}m until next checkpoint".format(distance))
            text = re.sub(clean_instructions,'',html_instructions)
            output =  ("STEP {} {} {}".format(i ,text,end_location))
            print(text)
            os.system('espeak "'+text+'"')
            while (distance > threshold):
                gps_location = c.recv(2048).decode('ascii')
                gps_coords = gps_location_to_tuple(gps_location)
                distance = get_coords_distance_meters(gps_coords, destination_coords) 
                gps_location = c.recv(2048).decode('ascii')
                print("{}m until next checkpoint".format(distance))
            i = i+1

def gps_location_to_tuple(gps_location_string):
    gps_location_string = (gps_location_string).replace("'", '"')
    json_obj = json.loads(gps_location_string)    
    gps_coords = (json_obj["fused"]["latitude"],json_obj["fused"]["longitude"]) 
    return gps_coords 

def get_coords_distance_meters(coords1, coords2):
    return haversine(coords1, coords2, unit=Unit.METERS)

main()
