from googlemaps import Client
import pprint
import re

mapService = Client(key='AIzaSyC9tAOmf2ismSx-ukPUotyCKF_r0eeY1V0')

StartDestination = input("Start?\n")
EndDestination = input("End?\n")

directions = mapService.directions( StartDestination , EndDestination, mode="walking")
directions = directions[0]
#pprint.pprint (directions)

i=1
for leg in directions['legs']:
    startAddress = leg['start_address']
    print ("Start Address:", startAddress)
    endAddress = leg['end_address']
    print ("End Address:", endAddress)
    for step in leg['steps']:
        html_instructions = step['html_instructions']
        end_location = step['end_location']
        clean_instructions = re.compile('<.*?>')
        text = re.sub(clean_instructions,'',html_instructions)
        print ("STEP {} {} {}".format(i ,text,end_location))
        #print(text,end_location)
        i = i+1

