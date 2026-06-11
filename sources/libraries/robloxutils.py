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
    "ModuleScript",
    "Script",
    "LocalScript",
    "TextButton",
    "TextLabel",
    "Camera",
    "Terrain",
    "SpawnLocation",
    "Workspace", ## This is the main one. so we not need him for now
]


def build_object_json(data):
    if data is None:
        return None

    if data.get("class") in blacklist_class or "Service" in data.get("class"):
        return None

    object_json = {
        "name": search_property("Name", data),
        "class": data.get("class"),
        "properties": {}
    }

    properties = data.find("Properties")

    if properties:
        for prop in properties:
            if is_property_blacklisted(prop):
                continue

            object_json["properties"][prop.get("name")] = prop.text

    print(object_json)

    return object_json

def is_property_blacklisted(property) -> bool:
    return property.get("name") in blacklist_properties

def search_property(name, item):
    if item is None:
        return
    
    for prop in item.find("Properties"):
        if prop.get("name") == name:
            return prop.text
    
    return None
