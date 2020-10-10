
import requests
import os
from datetime import datetime
import logging

# openrouteservices api key
KEY = '5b3ce3597851110001cf6248701a505f4a83471da001d266b2860ac6'


def start_open_route():
    print('Direction app')
    while True:
        choice = input('Press "Q" to quit or any other key to get directions: ').upper()
        if choice != 'Q':
            start = get_coords(get_user_data(message='\nChoose a starting point: '))
            print(start)
            end = get_coords(get_user_data(message='Choose a destination: '))
            print(end)
            get_directions(start, end)
        else:
            print('Thanks for using the program')
            break


def get_user_data(message):
    location = input(message)
    city = input('City?: ')
    state = input('State?: ')
    return f'{location} {city} {state}'


def get_coords(location):
    query = {'api_key': KEY, 'text': location}
    geo_url = 'https://api.openrouteservice.org/geocode/search'
    data = requests.get(geo_url, params=query).json()
    coords = data['features'][0]['geometry']['coordinates']
    return f'{str(coords[0])},{str(coords[1])}'


# TODO: program will crash if no route can be found
def get_directions(start, end):
    query = {'api_key': KEY, 'start': start, 'end': end}
    URL = 'https://api.openrouteservice.org/v2/directions/driving-car'
    '''foot-walking can be substituted for driving-car'''
    data = requests.get(URL, params=query).json()
    steps = data['features'][0]['properties']['segments'][0]['steps']

    count = 1
    for s in steps:
        distance = round((s['distance']*3.28)/5280, 2)
        direction = s['instruction']
        print(f'{count}. {direction} | {distance} miles.')
        count += 1


if __name__ == '__main__':
    start_open_route()

