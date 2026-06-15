import os
import xml.etree.ElementTree as ET
from colorama import Fore, Style, init
from tkinter import filedialog

from sources.libraries import godotutils
from sources.libraries import robloxutils

## Main variables
main_file = None
main_root = None
main_json = { 
    "Objects": [],
}

main_export_path = None
main_project_name = ""

## Functions
def search_file():
    global main_root, main_json

    main_file = filedialog.askopenfile(
        title="Open your roblox project file: ",
        filetypes=[
            ("Roblox file format: ", "*.rbxlx")
        ]
    )

    if main_file:
        print(f"Choosed file: {os.path.splitext(os.path.basename(main_file.name))[0]}.rbxlx")
        print("Exporting Items...")

        count = 0
        main_root = ET.parse(main_file).getroot()
        
        for item_class in main_root.findall(".//Item"):
            item_json = robloxutils.build_object_json(item_class)
            print(f"[{item_class.get("class")}]: Trying to converting to JSON...")
            if item_json is None:
                print(f"{Fore.RED}[{item_class.get("class")}]: Object/Class doesnt sopport yet!.{Fore.RESET}")
                continue

            main_json["Objects"].append(item_json)
            count += 1

            print(f"{Fore.GREEN}[{item_class.get("class")}]: Exported item: {count}{Fore.RESET}")
        
        print(f"\n{Fore.GREEN}Items exported [{count}]{Fore.RESET}")
    else:
        main_file = None

def search_export_project():
    global main_export_path

    main_export_path = filedialog.askdirectory(
        title="Select a dictionary to save the project files"
    )

    if main_export_path:
        godotutils.create_empty_project(main_export_path, 4.4, main_project_name)