import time

from colorama import Fore
from promise import Promise
from sources import sourcemap
from sources.libraries import godotutils
from sources.libraries import robloxutils

from tqdm import tqdm

builded = False

# def build_by_step():
#     global builded
#     if builded:
#         print("¡WARNING¡ Any changes you maked. gonna be rewrite again.")
#         print("Do you want rebuild the project?")
#         while True:
#             option = input("Choose [T/F]: ").strip().lower()
#             if option == "t":
#                 godotutils.delete_project()
#                 break
#             elif option == "f":
#                 return   
    
#     for step in tqdm(sourcemap.build_steps, desc="Building Project..."):
#         match step:
#             case "Creating base project":
#                 godotutils.create_empty_project(
#                     sourcemap.main_export_path, 
#                     sourcemap.main_version_project, 
#                     sourcemap.get_project_name()
#                 )

#                 time.sleep(3.5)
#             case "Finished":
#                 builded = True
#                 print("Finished")

def build_by_step():
    ## Making global builded for modify it
    global builded


    ## Making a checker first about was builded. in case yes. Rebuild from scratch
    # if builded:
    #     print(f"{Fore.RED}WARNING. ARE YOU SURE TO RE-BUILD THE PROJECT? {Fore.RESET}")
    #     print(f"{Fore.LIGHTYELLOW_EX}YOU CAN LOSE THE MODIFICATION WAS DO ON THE PROJECT. ARE YOU SURE ONCE AGAIN?{Fore.RESET}")

    #     # Now making a loop-option to the choose
    #     option = ""
    #     while True:
    #         option = input("Choose [T/F]").strip().lower()
    #         if option == "t":
    #             godotutils.delete_project()
    #             break
    #         elif option == "f":
    #             return
        

    ### Provitia princess
    ## Building the project files. using promise :money_month:
    new_promise = Promise(test_a)
    print(new_promise)
    print("Hehe")



def test_a(resolve, reject):
    print("Hi")
    time.sleep(2.0)
    resolve("RESOLVED")

