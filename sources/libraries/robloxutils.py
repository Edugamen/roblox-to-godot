blacklist_properties = [
    "Name",
    "HistoryId",
    "UniqueId",
    "SourceAssetId",
    "Tags",
    "PivotOffset"
    "Locked",
    "Massless",
    "EnableFluidForces",
    "CollisionGroup",
    "CollisionGroupId",
    "CanQuery",
    "CanTouch"
    "AudioCanCollide",
    "MaterialVariantSerialized",
]

blacklist_class = [
    "Decal",
    "Texture",
    "StarterGui",
    "Frame",
    "TextButton",
    "TextLabel",
    "Camera",
    "Terrain",
    "SpawnLocation"
    "Workspace" ## This is the main one. so we not need him for now
]


def build_object_json(data):
    if data is None:
        return None
    
    print(data)

    

    object_json = {
        "name": search_property("Name", data),
        "class": data.get("class"),
        "properties": {}
    }

   


    return object_json

def search_property(name, item):
    if item is None:
        return
    
    for prop in item.find("Properties"):
        if prop.get("name") == name:
            return prop.text
    
    return None
