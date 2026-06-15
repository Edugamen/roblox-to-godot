@tool
extends Node3D

@export_tool_button("Reload") 
var Reload: Callable = check_settings

@export_category("References")
@export var Collider: CollisionShape3D
@export var MeshInstance: MeshInstance3D

@export_category("Object")
var _object_color := Color.WHITE

@export var ObjectColor: Color:
	get:
		return _object_color
	set(value):
		_object_color = value
		check_settings()

@export_category("Colliders")
@export var can_collide: bool:
	set(value):
		check_settings()

func _ready() -> void:
	check_settings()

func check_settings():
	if !check_meshintance() or !check_collider():
		return

	Collider.disabled = not can_collide

	if MeshInstance.material_override == null:
		var mat := StandardMaterial3D.new()
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
