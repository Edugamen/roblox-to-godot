import os
import time
import xml.etree.ElementTree as ET
from tkinter import filedialog
from colorama import Fore

from sources.libraries import robloxutils

build_steps = [
    "Creating base project",
    "Finished"
]

## Variables

valid_godot_versions = [
    4.4,
    4.5,
    4.6,
]

## Class

class ExportState:
    def __init__(self):
        self.file = None
        self.root = None
        self.json = {"Objects": []}
        self.export_path = None
        self.project_name = "Unnamed project"
        self.version = None

state = ExportState()

## Functions
def search_file():
    state.file = filedialog.askopenfile(
        title="Open Roblox project",
        filetypes=[("Roblox file format", "*.rbxlx")]
    )

    if not state.file:
        return

    print(f"Loaded: {os.path.basename(state.file.name)}")

    state.root = ET.parse(state.file).getroot()
    state.json["Objects"] = []

    items = state.root.findall(".//Item")
    total = len(items)

    print(f"Found {total} objects")
    print("Converting...\n")

    for i, item in enumerate(items, start=1):
        print(f"[{i}/{total}] {item.get('class')}")

        obj = robloxutils.build_object_json(item)

        if obj is None:
            continue

        state.json["Objects"].append(obj)

    print(f"\n{Fore.GREEN}Converted: {len(state.json['Objects'])}{Fore.RESET}")

def search_export_project():
    state.export_path = filedialog.askdirectory(
        title="Select export folder"
    )

    if state.export_path:
        print("Export path:", state.export_path)

def set_project_version(version):
    if version not in valid_godot_versions:
        print("GODOT VERSION NOT AVARIABLE OR NON-EXIST")
        return
    
    state.version = version

## Utils

def get_roblox_file_name():
    if not has_roblox_file():
        return ""
    
    return str(os.path.splitext(os.path.basename(state.file.name))[0])

def get_project_name():
    if override_project_name:
        return override_project_name

    return get_roblox_file_name()

def set_project_name(name):
    global override_project_name
    override_project_name = name


def ready_to_build():
    return all([
        state.file,
        state.export_path,
        state.version in valid_godot_versions
    ])

def has_roblox_file():
    return state.file is not None

def has_project_export():
    return state.export_path is not None

def has_version_selected():
    return state.version in valid_godot_versions