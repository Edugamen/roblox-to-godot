import time

from sources import sourcemap
from sources.libraries import godotutils
from sources.libraries import robloxutils

from tqdm import tqdm

builded = False

def build_by_step():
    global builded
    if builded:
        print("¡WARNING¡ Any changes you maked. gonna be rewrite again.")
        print("Do you want rebuild the project?")
        while True:
            option = input("Choose [T/F]: ").strip().lower()
            if option == "t":
                godotutils.delete_project()
                break
            elif option == "f":
                return   
    
    for step in tqdm(sourcemap.build_steps, desc="Building Project..."):
        match step:
            case "Creating project":
                godotutils.create_empty_project(
                    sourcemap.main_export_path, 
                    sourcemap.main_version_project, 
                    sourcemap.get_project_name()
                )

                time.sleep(3.5)
            case "Finished":
                builded = True
                print("Finished")
