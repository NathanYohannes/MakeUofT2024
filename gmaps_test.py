import googlemaps # pip install googlemaps
import requests
import json
import pprint

#https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood&key=
API_KEY = 'AIzaSyC9tAOmf2ismSx-ukPUotyCKF_r0eeY1V0'

res = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=43.6607744,-79.3965795&destination=43.6490343,-79.3964434&mode=walking&key='+API_KEY)

r = res.json()
pprint.pprint(r['routes'])

#print(r['routes'])

#map_client = googlemaps.Client(API_KEY)