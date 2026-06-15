import os
import time
import platform
import xml.etree.ElementTree as ET

from sources import sourcemap
from sources import utilities
from colorama import Fore, Style, init

## Variables

opcion_choosed = 0
system = platform.system()

## Functions

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:  # Linux y macOS
        os.system("clear")

def main_cycle_option():
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
                              Created by DevEdugamen  ({utilities.get_version()})              
            

    {Fore.RESET}""")
    print("Small program converting roblox place to a godot project semi-completly")
    print("Please choose an option to configurate...\n")

    # Place File
    message = f"{Fore.RED} File doesnt exist {Fore.RESET}"
    if sourcemap.has_roblox_file():
        message = f"{Fore.GREEN}{sourcemap.get_roblox_file_name()}.rbxlx{Fore.RESET}"
    
    print(f"[1] - Roblox File: {message}")

    # Exported Project
    message = f"{Fore.RED} Project Folder doesnt choosed {Fore.RESET}"
    if sourcemap.has_project_export():
        message = f"{Fore.GREEN}{sourcemap.main_export_path}{Fore.RESET}"
    
    print(f"[2] - Project Export Folder: {message}")

    # Godot Version
    message = f"{Fore.RED} Version no choosed yet. {Fore.RESET}"
    if sourcemap.has_version_selected():
        message = f"{Fore.GREEN}{sourcemap.main_export_path}{Fore.RESET}"
    
    print(f"[3] - Project Version: {message}")

    print("[4] - Exit")

    while True:
        opcion_choosed = int(input("Choose a opcion: "))

        clear_console()
        match opcion_choosed:
            case 1:
                sourcemap.search_file()
                time.sleep(4.0)
                main_cycle_option()
                break
            case 2:
                sourcemap.search_export_project()
                main_cycle_option()
                break
            case 3:
                pass
            case 4:
                break

            case _:
                print("UNKNOW OPCION")
        
            
    

## Main


main_cycle_option()

# print("[1] - Choose the file .rbxlx ")
# search_file()

# print("\n\n[2] - Insert a name for the project")
# main_project_name = str(input("Project Name: "))