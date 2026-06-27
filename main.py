import os
import time
import platform
import xml.etree.ElementTree as ET

from sources import ui
from sources import sourcemap
## Variables

message = ""
opcion_choosed = 0
system = platform.system()

## Functions

# def clear_console():
#     if platform.system() == "Windows":
#         os.system("cls")
#     else:  # Linux y macOS
#         os.system("clear")

# def misc_cycle_option():
#     global message
#     global opcion_choosed

#     ## Resetiing variables
#     message = ""
#     opcion_choosed = 0

#     ## Cleanning console log. to much better on visuals lol
#     clear_console()

#     print("""
#     #############################################################
#     #                                                           #
#     #   ████      ████  ████████████  ██████████    ████████    #
#     #   ██  ██  ██  ██       ██       ██          ██            #
#     #   ██    ██    ██       ██       ██████████  ██            #
#     #   ██          ██       ██               ██  ██            #
#     #   ██          ██  ████████████  ██████████    ████████    #
#     #                                                           #
#     #############################################################
#     """)

#     # Override Project Name
#     message = "[1] - Override Project Name: "
#     if sourcemap.has_roblox_file():
#         if sourcemap.override_project_name:
#             message += f"{Fore.GREEN}{sourcemap.override_project_name}{Fore.RESET}"
#         else:
#             message += f"{Fore.YELLOW}{sourcemap.get_roblox_file_name()} (its the name by default on the .rbxlx file) you can still change it{Fore.RESET}"
#     else:
#         message += f"{Fore.RED}YOU CANNOT OVERRIDE THE PROJECT NAME UNTIL YOU OPEN A .RBLXL FILE{Fore.RESET}"

#     print(message)

#     if sourcemap.has_roblox_file() and sourcemap.override_project_name is not None:
#         print("[2]: Reset project Name")

#     # Return back to main
#     if sourcemap.override_project_name is not None:
#         print("[3]: Go back to Main")
#     else:
#         print("[2]: Go back to Main")

#     while True:
#         try:
#             opcion_choosed = int(input("Choose an option: "))
#         except ValueError:
#             print("Invalid option")
#             continue

#         match opcion_choosed:
#             case 1:
#                 if sourcemap.has_roblox_file():
#                     temp_override_name = str(input("Insert a name to override the project name: "))
#                     sourcemap.set_project_name(temp_override_name)

#                     misc_cycle_option()
#                     break
#             case 2:
#                 if sourcemap.has_roblox_file() and sourcemap.override_project_name is not None:
#                     sourcemap.set_project_name(None)
                    
#                     print("Removed")
#                     time.sleep(1.1)

#                     misc_cycle_option()
#                     break
#                 else:
#                     main_cycle_option()
#                     break
#             case 3:
#                 if sourcemap.has_roblox_file() and sourcemap.override_project_name is not None:
#                     main_cycle_option()
#                     break
#                 else:
#                     pass
#             case _:
#                 print("UNKNOW OPCION")


#     print(message)

#     # Misc
#     print("[5] - Misc")

#     # Exit
#     print("[6] - Exit")

#     # Cycle loop for the opcions
#     while True:
#         try:
#             opcion_choosed = int(input("Choose an option: "))
#         except ValueError:
#             print("Invalid option")
#             continue

#         clear_console()
#         match opcion_choosed:
#             case 1:
#                 sourcemap.search_file()
#                 time.sleep(3.25)
#                 main_cycle_option()
#                 break
#             case 2:
#                 sourcemap.search_export_project()
#                 main_cycle_option()
#                 break
#             case 3:
#                 temp_version = float(input("Select Godot Project Version: "))
#                 if temp_version not in sourcemap.valid_godot_versions:
#                     raise ValueError(
#                         "Unsopported Godot Version"
#                     )
                
#                 sourcemap.set_project_version(temp_version)
#                 main_cycle_option()
#                 temp_version = None
#                 break
#             case 4:
#                 if not sourcemap.ready_to_build():
#                     print(f"{Fore.RED}[x] ERROR:{Fore.RESET} the project its not ready to build. PLEASE check the requirements")
#                     time.sleep(4.2)
#                     main_cycle_option()
#                     break
                    
#                 print("Building...")
#                 build.build_by_step()
#                 time.sleep(3)
#                 main_cycle_option()
#                 break
#             case 5:
#                 misc_cycle_option()
#                 break
#             case 6:
#                 break

#             case _:
#                 print("UNKNOW OPCION")
        
def ask_int(prompt="Choose option: "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, try again")

def ask_str(prompt="Choose option: "):
    while True:
        try:
            return str(input(prompt))
        except ValueError:
            print("Invalid input, try again")

def run_misc():
    is_running = True
    while is_running:
        ui._show_misc()
        option = ask_int()

        match option:
            case 1:
                if sourcemap.has_roblox_file():
                    sourcemap.state.project_name = ask_str("Insert a project name: ")
            case 2:
                if sourcemap.has_roblox_file() and sourcemap.state.project_name != sourcemap.get_roblox_file_name():
                    sourcemap.state.project_name = sourcemap.get_roblox_file_name()
                else:
                    is_running = False
            case 3: is_running = False


def run():
    is_running = True

    while is_running:
        ui._show_mainmenu()
        option = ask_int()

        match option:
            case 1:
                sourcemap.search_file()
            case 2:
                sourcemap.search_export_project()
            case 3:
                print("4.4, 4.5, 4.6")
                sourcemap.set_project_version(ask_int("Choose an Engine: "))
            case 4: pass
            case 5: run_misc()
            case 6: is_running = False

    

# ## Main

# main_cycle_option()

# ## build.build_by_step()

if __name__ == '__main__':
    run()