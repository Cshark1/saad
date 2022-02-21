import requests
import xml.etree.ElementTree as ET
import os

api_key = os.environ.get("API_KEY")

owned_games_url = "https://steamcommunity.com/profiles/{}/games?tab=all&xml=1"
path = "https://www.steamgriddb.com/api/v2/grids/steam/{}"
steam_id_64 = "76561198267351741"
game_id = "271590"
nsfw = "false"

owned_games_xml = ET.fromstring(requests.get(owned_games_url.format(steam_id_64)).text)
for x in owned_games_xml[2]:
     print(x[0].text)


#r = requests.get(path.format(game_id), headers={"Authorization": "Bearer {}".format(api_key)},
#                 params={"types": "animated", "nsfw": nsfw})

#print(r.json())
