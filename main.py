import os
import time
import platform
import xml.etree.ElementTree as ET

from sources import build
from sources import sourcemap
from sources import utilities
from colorama import Fore

## Variables

message = ""
opcion_choosed = 0
system = platform.system()

## Functions

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:  # Linux y macOS
        os.system("clear")

def misc_cycle_option():
    global message
    global opcion_choosed

    ## Resetiing variables
    message = ""
    opcion_choosed = 0

    ## Cleanning console log. to much better on visuals lol
    clear_console()

    print("""
    #############################################################
    #                                                           #
    #   ████      ████  ████████████  ██████████    ████████    #
    #   ██  ██  ██  ██       ██       ██          ██            #
    #   ██    ██    ██       ██       ██████████  ██            #
    #   ██          ██       ██               ██  ██            #
    #   ██          ██  ████████████  ██████████    ████████    #
    #                                                           #
    #############################################################
    """)

    # Override Project Name
    message = "[1] - Override Project Name: "
    if sourcemap.has_roblox_file():
        if sourcemap.override_project_name:
            message += f"{Fore.GREEN}{sourcemap.override_project_name}{Fore.RESET}"
        else:
            message += f"{Fore.YELLOW}{sourcemap.get_roblox_file_name()} (its the name by default on the .rbxlx file) you can still change it{Fore.RESET}"
    else:
        message += f"{Fore.RED}YOU CANNOT OVERRIDE THE PROJECT NAME UNTIL YOU OPEN A .RBLXL FILE{Fore.RESET}"

    print(message)

    if sourcemap.has_roblox_file() and sourcemap.override_project_name is not None:
        print("[2]: Reset project Name")

    # Return back to main
    if sourcemap.override_project_name is not None:
        print("[3]: Go back to Main")
    else:
        print("[2]: Go back to Main")

    while True:
        try:
            opcion_choosed = int(input("Choose an option: "))
        except ValueError:
            print("Invalid option")
            continue

        match opcion_choosed:
            case 1:
                if sourcemap.has_roblox_file():
                    temp_override_name = str(input("Insert a name to override the project name: "))
                    sourcemap.set_project_name(temp_override_name)

                    misc_cycle_option()
                    break
            case 2:
                if sourcemap.has_roblox_file() and sourcemap.override_project_name is not None:
                    sourcemap.set_project_name(None)
                    
                    print("Removed")
                    time.sleep(1.1)

                    misc_cycle_option()
                    break
                else:
                    main_cycle_option()
                    break
            case 3:
                if sourcemap.has_roblox_file() and sourcemap.override_project_name is not None:
                    main_cycle_option()
                    break
                else:
                    pass
            case _:
                print("UNKNOW OPCION")

def main_cycle_option():
    global opcion_choosed
    global message 
    
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

    message = "" # Cleening up the message

    # Place File
    message = f"{Fore.RED} File doesnt exist {Fore.RESET}" ## Setting by default file doesnt choosed
    if sourcemap.has_roblox_file():
        message = f"{Fore.GREEN}{sourcemap.get_roblox_file_name()}.rbxlx{Fore.RESET}" ## Incase we open the .rbxlx file. showing the name
    
    print(f"[1] - Roblox File: {message}")

    # Exported Project
    message = f"{Fore.RED} Project Folder doesnt choosed {Fore.RESET}" ## Cleening up and showing a error we doesnt choosed a export folder path
    if sourcemap.has_project_export():
        message = f"{Fore.GREEN}{sourcemap.main_export_path}{Fore.RESET}" ## In case we selected a folder. showing the path
    
    print(f"[2] - Project Export Folder: {message}")

    # Godot Version
    message = f"{Fore.RED} Version no choosed yet. {Fore.RESET}" ## Cleening up and making message for the godot project version
    if sourcemap.has_version_selected():
        message = f"{Fore.GREEN}{sourcemap.main_version_project}{Fore.RESET}" ## In case we choosed a version. showing the version
    
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

    print(message)

    # Misc
    print("[5] - Misc")

    # Exit
    print("[6] - Exit")

    # Cycle loop for the opcions
    while True:
        try:
            opcion_choosed = int(input("Choose an option: "))
        except ValueError:
            print("Invalid option")
            continue

        clear_console()
        match opcion_choosed:
            case 1:
                sourcemap.search_file()
                time.sleep(3.25)
                main_cycle_option()
                break
            case 2:
                sourcemap.search_export_project()
                main_cycle_option()
                break
            case 3:
                temp_version = float(input("Select Godot Project Version: "))
                if temp_version not in sourcemap.valid_godot_versions:
                    raise ValueError(
                        "Unsopported Godot Version"
                    )
                
                sourcemap.set_project_version(temp_version)
                main_cycle_option()
                temp_version = None
                break
            case 4:
                if not sourcemap.ready_to_build():
                    print(f"{Fore.RED}[x] ERROR:{Fore.RESET} the project its not ready to build. PLEASE check the requirements")
                    time.sleep(4.2)
                    main_cycle_option()
                    break
                    
                print("Building...")
                build.build_by_step()
                time.sleep(3)
                main_cycle_option()
                break
            case 5:
                misc_cycle_option()
                break
            case 6:
                break

            case _:
                print("UNKNOW OPCION")
        
            
    

## Main

main_cycle_option()