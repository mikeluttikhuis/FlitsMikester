import requests
import json
import config

FM_URL = "https://tesla.flitsmeister.nl/teslaFeed.json"
NOTIFY_URL = config.NOTIFY_URL
ROADS = ["A1", "A35", "N342"]
speedtrap = False

r = requests.get(FM_URL)
r = json.loads(r.text)

for feature in r['features']:
    if (feature['properties']['type_description'] == "speedtrap" and
    feature['properties']['country_code'] == "nl" and
    feature['properties']['road'] in ROADS):
        speedtrap = True
        road = feature['properties']['road']
        direction = feature['properties']['direction']
        data = f"{road}, {direction}"
        requests.post(NOTIFY_URL, data=data)

if not speedtrap:
    data = "Geen flitsers op woon-werk route"
    requests.post(NOTIFY_URL, data=data)
