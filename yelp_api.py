

import requests
from api_starters.openroute_api import get_coords, get_directions



Key = 'zwNR-_GO-ShcVj2Gc9RheHSCG4rIitXhhm5juTyEGBFExzJzxqebyhcy6wQbkMSxAO-sUzLO3RO88c86jqTn87v7Q5e4X8XgNY7Abn2-B8SK3jwFg8d9LXllPdeBX3Yx'

url = "https://api.yelp.com/v3/businesses/search"

'''
search types:
Business search || /business/search
'''

current_location = get_coords(input("Current location: "))
search_term = 'pizza'
category = 'restaurants'
location = 'St. Louis Park,MN'
price = 3
headers = {'Authorization': 'Bearer %s' % Key}
query = {'term': search_term, 'categories': category, 'location': location, 'radius': 10000, 'price': price, 'limit': 20}

data = requests.get(url, params=query, headers=headers).json()
print(data)
# parsed = json.loads(data.text)
count = 1
business_options = data['businesses']
for b in business_options:
    print(f'{count}. {b["name"]} || {b["categories"][0]["title"]} || Rating:{b["rating"]}')
    print('address:', f'{" ".join(b["location"]["display_address"])} || Phone: {b["phone"]}\n')
    count += 1

user_input = input('Choose a venue by number: ')

# get coordinates
coords_long = business_options[int(user_input)-1]['coordinates']['longitude']
coords_lat = business_options[int(user_input)-1]['coordinates']['latitude']
destination_coords = f'{coords_long},{coords_lat}'
print(destination_coords)

get_directions(current_location,destination_coords)






