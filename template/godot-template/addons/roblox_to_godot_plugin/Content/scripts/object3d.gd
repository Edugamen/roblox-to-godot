@tool
extends Node3D

@export_tool_button("Reload") 
var Reload: Callable = check_settings

@export_category("References")
@export var Collider: CollisionShape3D
@export var MeshInstance: MeshInstance3D

@export_category("Object")
@export var ObjectColor: Color

@export_category("Colliders")
@export var can_collide: bool = true:
	set(value):
		if not check_collider():
			printerr("THIS PLACEHOLDER DOESNT HAVE COLLIDER")
			return
			
		can_collide = value
		check_settings()

func _ready() -> void:
	check_settings()

func check_settings():
	if !check_meshintance() or !check_collider():
		return
	
	Collider.disabled = not can_collide
	if MeshInstance.material_override:
		if !MeshInstance.material_override.resource_local_to_scene:
			var mat = MeshInstance.material_override.duplicate()
			mat.resource_local_to_scene = true
			MeshInstance.material_override = mat

		MeshInstance.material_override.albedo_color = ObjectColor

func check_meshintance() -> bool:
	var found_it = false
	
	for v in get_children():
		if v is MeshInstance3D:
			found_it = true
			if MeshInstance != v:
				MeshInstance = v
			break
	
	return found_it


func check_collider() -> bool:
	var found_it = false
	
	for v in get_children():
		if v is StaticBody3D:
			for b in v.get_children():
				if b is CollisionShape3D:
					found_it = true
					if Collider != b:
						Collider = b
					break
	
	return found_it
