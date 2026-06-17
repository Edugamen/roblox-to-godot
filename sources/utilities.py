from tqdm import tqdm
import requests

## Functions

def create_progress():
    x = 1
    for i in tqdm(range(0, 200000)):
        for x in range(0, 10000):
            x *= 4

def get_version():
    data = requests.get(
        "https://api.github.com/repos/Edugamen/roblox-to-godot/commits"
    ).json()[0]["sha"][:7]

    return str(data)