import os
import platform

from colorama import Fore
from sources import utilities, sourcemap

## Functions

def _show_title():
    clear_console()
    print(f"""{Fore.MAGENTA}
        ###############################################################################
        #                                                                             #
        #  █████████     ███████   █████████  ███         ███████    ███         ███  #
        #  ███     ███ ███     ███ ███    ███ ███       ███     ███    ███     ███    #
        #  ███     ███ ███     ███ █████████  ███       ███     ███      ███ ███      #
        #  █████████   ███     ███ ███    ███ ███       ███     ███       █████       #
        #  ███     ███ ███     ███ ███    ███ ███       ███     ███    ███     ███    #
        #  ███     ███   ███████    ████████  █████████   ███████    ███         ███  #
        #                                                                             #
        #                        ███████████   █████                                  #
        #                            ███     ███   ███                                #
        #                            ███     ███   ███                                #
        #                            ███     ███   ███                                #   
        #                            ███       █████                                  #
        #                                                                             #
        #    ██████       ████████   █████████     ████████   ███████████████         #
        #  ███     ███  ███      ███ ███     ███ ███      ███       ███               #
        #  ███          ███      ███ ███     ███ ███      ███       ███               #
        #  ███          ███      ███ ███     ███ ███      ███       ███               #
        #  ███   █████  ███      ███ ███     ███ ███      ███       ███               #
        #  ███      ███ ███      ███ ███     ███ ███      ███       ███               #
        #    ████████     ████████   █████████     ████████         ███               #
        #                                                                             #    
        #                                                                             #                                                            
        #                                                                             #    
        ###############################################################################
                          Created by DevEdugamen  git-version ({utilities.get_version()})    
    {Fore.RESET}""")

    print("Small program converting roblox place to a godot project semi-completly")
    print("Please choose an option to configurate...\n")

def _show_misc():
    _show_title()
    message = "" 

    # Override Project
    message = "[1] - Override Project Name: "
    if sourcemap.has_roblox_file():
        if sourcemap.state.project_name == sourcemap.get_roblox_file_name():
            message += f"{Fore.YELLOW}{sourcemap.get_roblox_file_name()} (its the name by default on the .rbxlx file) you can still change it{Fore.RESET}"
        else: 
            message += f"{Fore.GREEN}{sourcemap.state.project_name}{Fore.RESET}"
    else:
        message += f"{Fore.RED}LOCKED{Fore.RESET}"
    
    print(message)

    # Exit
    if sourcemap.has_roblox_file() and sourcemap.state.project_name == sourcemap.get_roblox_file_name():
        message = "[2]: "
    else:
        message = "[3]: "
    
    message += "Go back to main"
    print(message)


def _show_mainmenu():
    _show_title()
    message = ""

    # Place File
    message = f"{Fore.RED} File doesnt exist {Fore.RESET}" ## Setting by default file doesnt choosed
    if sourcemap.has_roblox_file():
        message = f"{Fore.GREEN}{sourcemap.get_roblox_file_name()}.rbxlx{Fore.RESET}" ## Incase we open the .rbxlx file. showing the name
    
    print(f"[1] - Roblox File: {message}")

    # Exported Project
    message = f"{Fore.RED} Project Folder doesnt choosed {Fore.RESET}" ## Cleening up and showing a error we doesnt choosed a export folder path
    if sourcemap.has_project_export():
        message = f"{Fore.GREEN}{sourcemap.state.export_path}{Fore.RESET}" ## In case we selected a folder. showing the path
    
    print(f"[2] - Project Export Folder: {message}")

    # Godot Version
    message = f"{Fore.RED} Version no choosed yet. {Fore.RESET}" ## Cleening up and making message for the godot project version
    if sourcemap.has_version_selected():
        message = f"{Fore.GREEN}{sourcemap.state.version}{Fore.RESET}" ## In case we choosed a version. showing the version
    
    print(f"[3] - Project Version: {message}")

    # Build project
    message = "[4] - " ## Rewriting the message. i dont use more variables just for a visual thing so i use one variable for everything.
    if sourcemap.ready_to_build():
        message += f"{Fore.GREEN}¡Build Project!{Fore.RESET}"
    else:
        message += f"{Fore.RED}Missing Steps to build the project{Fore.RESET}"

        if not sourcemap.has_roblox_file():
            message += f"\n     {Fore.RED}[x]: Missing roblox file{Fore.RESET}"
            
        if not sourcemap.has_project_export():
            message += f"\n     {Fore.RED}[x]: Missing export folder path{Fore.RESET}"
            
        if not sourcemap.has_version_selected():
            message += f"\n     {Fore.RED}[x]: Missing version selected{Fore.RESET}"

    print(message) # Building Project
    print("[5] - Misc") # Misc
    print("[6] - Exit") # Exit

## Utilities
def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

