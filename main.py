from tkinter import filedialog
import xml.etree.ElementTree as ET

from sources.libraries import godotutils
from sources.libraries import robloxutils

main_root = None

def search_file():
    global main_root

    tempfile = filedialog.askopenfile(
        title="Open your roblox project file: ",
        filetypes=[
            ("Roblox file format: ", "*.rbxlx")
        ]
    )

    if tempfile:
        main_root = ET.parse(tempfile).getroot()
        
        for item_class in main_root.findall(".//Item"):
            
            print(robloxutils.build_object_json(item_class))

search_file()