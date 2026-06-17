import re
import random
import base64

import shutil
from pathlib import Path

## Variables
root_path = Path(__file__).parent.parent.parent
godot_template = root_path / "template" / "godot-template"

project_file = None

prefabs_path = {
    "Cube": "res://placeholder_objects/cube.tscn",
    "Cylinder": "res://placeholder_objects/cylinder.tscn"
}

valid_godot_versions = [
    4.4,
    4.5,
    4.6,
]

## Godot Projects

def create_empty_project(to_path, version, project_name):
    global project_file

    if version not in valid_godot_versions:
        raise ValueError(
            f"Unsupported Godot version: {version}"
        )
    
    if exist_project_file(to_path, project_name):
        project_name = get_available_project_name(
            to_path,
            project_name
        )

    
    destination = Path(to_path) / project_name

    shutil.copytree(
        godot_template,
        destination
    )

    new_destination = destination.parent / project_name
    destination.rename(new_destination)

    project_file = destination

    content = (new_destination / "project.godot").read_text(encoding="utf-8")

    ## Update Project Name
    content = re.sub(
        r'config/name="[^"]*"',
        f'config/name="{project_name}"',
        content
    )

    ## Update Assembly Project Name
    content = re.sub(
        r'project/assembly_name="[^"]*"',
        f'project/assembly_name="{project_name}"',
        content
    )

    ## Update Version file
    content = re.sub(
        r'config/features=PackedStringArray\(".*?"\)',
        f'config/features=PackedStringArray("{version}")',
        content
    )

    (new_destination / "project.godot").write_text(
        content,
        encoding="utf-8"
    )
        
    print(f"[godotutils] godot project created with version: {version} LTS")

def exist_project_file(path, project_name):
    project_path = Path(path) / project_name

    return (
        project_path.exists() and
        project_path.is_dir() and
        (project_path / "project.godot").exists()
    )

def delete_project():
    global project_file

    if project_file is None:
        return False

    if not project_file.exists():
        project_file = None
        return False

    shutil.rmtree(project_file)

    project_file = None
    return True

## Misc
def get_available_project_name(path, project_name):
    base_path = Path(path)

    if not (base_path / project_name).exists():
        return project_name

    counter = 1

    while (base_path / f"{project_name}_{counter}").exists():
        counter += 1

    return f"{project_name}_{counter}"

def generate_uid():
    uid = random.getrandbits(64)
    uid_bytes = uid.to_bytes(8, "big")
    return base64.b32encode(uid_bytes).decode().lower().rstrip("=")