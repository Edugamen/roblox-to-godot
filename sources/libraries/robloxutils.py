# Blacklist properties and classes
blacklist_properties = [
    "Name",
    "HistoryId",
    "UniqueId",
    "SourceAssetId",
    "Tags",
    "PivotOffset",
    "Locked",
    "Massless",
    "EnableFluidForces",
    "CollisionGroup",
    "CollisionGroupId",
    "CanQuery",
    "CanTouch",
    "AudioCanCollide",
    "MaterialVariantSerialized",
]

blacklist_class = [
    "Decal",
    "Texture",
    "StarterGui",
    "Frame",
    "UIGradient",
    "UICorner",
    "UIPadding",
    "StudioData",
    "StarterPlayer"
    "Packages",
    "AvatarSettings",
    "Selection",
    "Sky",
    "BlockLuaScripts",
    "ServerStorage",
    "BlurEffect",
    "DepthOfFieldEffect",
    "Atmosphere",
    "Teams",
    "VirtuaInputManager"
    "ModuleScript",
    "Script",
    "LocalScript",
    "TextButton",
    "TextLabel",
    "Camera",
    "Terrain",
    "SpawnLocation",
    "ReplicatedStorage",
    "ReplicatedFirst",
    "Debris",
    "StarterPack",
    "StarterCharacterScripts",
    "ChatInputBarConfiguration",
    "Lighting",
    "BlockLuaScripts",
    "SunRays",
    "BubbleChatConfiguration",
    "ChatWindowConfiguration",
    "Players",
    "Chat",
    "Workspace", ## This is the main one. so we not need him for now
]

current_id = 0

## Functions
def build_object_json(data, parent_id=0):
    if data is None:
        return None

    if (
        data.get("class") in blacklist_class
        or data.get("class", "").endswith("Service")
    ):
        return None

    object_id = generate_id()

    object_json = {
        "Id": object_id,
        "ParentId": parent_id,

        "Name": search_property("Name", data),
        "ClassType": data.get("class"),

        "Properties": {}
    }

    properties = data.find("Properties")

    if properties:
        for prop in properties:
            if is_property_blacklisted(prop):
                continue

            object_json["Properties"][prop.get("name")] = prop.text

    return object_json

def export_item(item, parent_id=0, output=None):
    if output is None:
        output = []

    obj = build_object_json(item, parent_id)

    if obj is None:
        return output

    output.append(obj)

    my_id = obj["Id"]

    for child in item.findall("Item"):
        export_item(child, my_id, output)

    return output

def search_property(name, item):
    if item is None:
        return
    
    for prop in item.find("Properties"):
        if prop.get("name") == name:
            return prop.text
    
    return None

## Utils
def generate_id():
    global current_id

    current_id += 1
    return current_id

def is_property_blacklisted(property) -> bool:
    return property.get("name") in blacklist_properties

