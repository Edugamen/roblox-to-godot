import requests

## Functions

def get_version():
    data = requests.get(
        "https://api.github.com/repos/Edugamen/roblox-to-godot/commits"
    ).json()[0]["sha"][:7]

    return str(data)