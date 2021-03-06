import requests
from termcolor import colored
import xml.etree.ElementTree as ET
import re
import os

api_key = os.environ.get("API_KEY")

steam_path = "/home/cshark/.steam/root/{}"
games = []
owned_games_url = "https://steamcommunity.com/profiles/{}/games?tab=all&xml=1"
path = "https://www.steamgriddb.com/api/v2/grids/steam/{}"
steam_id_64 = "76561198267351741"
game_id = "271590"
nsfw = "false"
game_id_pattern = re.compile("\d+")

while True:
    api_key = input(colored("Enter API key (Available at https://www.steamgriddb.com/profile/preferences): ", "white"))
    r = requests.get("https://www.steamgriddb.com/api/v2/grids/steam/720",
                     headers={"Authorization": "Bearer {}".format(api_key)})
    if r.status_code == 401:
        print(colored("Invalid API Key!", "red"))
    else:
        print(colored("The API key is valid!", "green"))
        break

print()

while True:
    response = input(colored("Do you want nsfw images? [Y]es/[N]o: ", "white"))
    if response.lower() == "y" or response.lower() == "yes":
        nsfw = "true"
        print(colored("NSFW content will be included in the results!", "green"))
        break
    elif response.lower() == "n" or response.lower() == "no":
        nsfw = "false"
        print(colored("NSFW content will be excluded from the results!", "green"))
        break
    else:
        print(colored("Please respond with [Y]es/[N]o!", "red"))

print()
print(colored("Getting a list of all games on your account...", "yellow"))
print()
for item in os.listdir(steam_path.format("appcache/librarycache")):
    res = game_id_pattern.findall(item)
    if not res:
        continue
    if game_id_pattern.findall(item)[0] not in games:

        games.append(game_id_pattern.findall(item)[0])
print(colored("List acquired successfully!", "green"))
print()

for gid in games:
    print(colored("Getting image for gameid {}".format(gid), "yellow"))
    req = requests.get(path.format(gid), headers={"Authorization": "Bearer {}".format(api_key)},
                       params={"types": "animated", "nsfw": nsfw})
    if req.status_code == 404:
        print(colored("Gameid {} not found".format(gid), "red"))
    elif not req.json()["data"]:
        print(colored("No artwork found for game {}".format(gid), "red"))
    else:
        print(req.json()["data"][0]["url"])
    print()


