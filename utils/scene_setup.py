import bpy
import os
import math
def clear_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)

def set_background_color(config):
    bpy.context.scene.world.use_nodes = True
    bg_node = bpy.context.scene.world.node_tree.nodes['Background']
    bg_node.inputs['Color'].default_value = config.background_color

def set_transparent_background():
    bpy.context.scene.render.film_transparent = True
    bpy.context.scene.render.image_settings.color_mode = 'RGBA'

def euler_transform_to_obj(obj, config):
    from math import radians

    rot_deg = float(config.get('rot_deg', 0))
    rot_axis = config.get('rot_axis', 'Y').lower()
    scale_factor = float(config.get('scale', 1))

    rot_rad = radians(rot_deg)
    setattr(obj.rotation_euler, rot_axis, rot_rad)
    obj.scale = (scale_factor, scale_factor, scale_factor)

def print_mesh_bounds(obj):
    min_coords = [min([v.co[i] for v in obj.data.vertices]) for i in range(3)]
    max_coords = [max([v.co[i] for v in obj.data.vertices]) for i in range(3)]
    print(f"Mesh Bounds:\nMin: {min_coords}\nMax: {max_coords}")


def setup_lights(config):
    light_positions = config.get('light_positions')
    if not light_positions:
        print("No light positions specified in configuration.")
        return

    print("Setting up lights...")
    num_lights = len(light_positions)

    # Get light parameters from config
    light_energies = config.get('light_energies', [100000.0])
    light_types = config.get('light_types', ['POINT'])
    light_radii = config.get('light_radii', [1.0])
    light_colors = config.get('light_colors', [(1.0, 1.0, 1.0)])
    light_cast_shadows = config.get('light_cast_shadows', [True])

    # Ensure parameters are lists of the correct length
    light_energies = match_parameter_length(light_energies, num_lights, 'light energies')
    light_types = match_parameter_length(light_types, num_lights, 'light types')
    light_radii = match_parameter_length(light_radii, num_lights, 'light radii')
    light_colors = match_parameter_length(light_colors, num_lights, 'light colors')
    light_cast_shadows = match_parameter_length(light_cast_shadows, num_lights, 'light_cast_shadows')

    for position,energy,light_type,light_radius,light_color,cast_shadows in zip(light_positions,light_energies,light_types,light_radii,light_colors,light_cast_shadows):
        create_light(position, energy, light_type, light_radius, light_color, cast_shadows)

def create_light(position, energy, light_type='POINT', light_radius=1.0, light_color=(1.0, 1.0, 1.0),cast_shadows=True):
    light_data = bpy.data.lights.new(name=f"Light_{light_type}", type=light_type)
    light_data.energy = energy
    light_data.color = light_color

    # Set light-specific properties
    if light_type == 'POINT':
        light_data.shadow_soft_size = light_radius
    elif light_type == 'SUN':
        light_data.angle = math.radians(light_radius)  # For sun size in degrees
    elif light_type == 'SPOT':
        light_data.shadow_soft_size = light_radius
        light_data.spot_size = math.radians(45.0)  # Default spot angle
        light_data.spot_blend = 0.15
    elif light_type == 'AREA':
        light_data.size = light_radius  # For square area lights
    else:
        print(f"Unsupported light type '{light_type}'. Defaulting to 'POINT'.")
        light_data.shadow_soft_size = light_radius

    # Set whether the light casts shadows
    print(cast_shadows)
    light_data.use_shadow = False

    # Create light object and link to scene
    light_object = bpy.data.objects.new(name=f"Light_{light_type}", object_data=light_data)
    bpy.context.collection.objects.link(light_object)
    light_object.location = position

def match_parameter_length(param_list, num_lights, param_name):
    """
    Ensures the parameter list matches the number of lights.
    If the list has one item, it's duplicated. Otherwise, lengths must match.
    """
    if len(param_list) == 1:
        return param_list * num_lights
    elif len(param_list) != num_lights:
        raise ValueError(f"The number of {param_name} ({len(param_list)}) must match the number of light positions ({num_lights}) or be a single value.")
    return param_list


def load_object(config):
    obj_file_path = config['object_file_path']
    if not os.path.exists(obj_file_path):
        raise FileNotFoundError(f"File not found: {obj_file_path}")
    bpy.ops.wm.obj_import(filepath=obj_file_path)
    obj = bpy.context.selected_objects[0]

    euler_transform_to_obj(obj, config)
    print_mesh_bounds(obj)
    return obj

def set_scene_units(config):
    scene = bpy.context.scene
    # Set the unit system to 'METRIC'
    scene.unit_settings.system = 'METRIC'
    units = config.get("scene_units")
    if units == "MILLIMETERS":
        scene.unit_settings.scale_length = 0.001  # 1 meter = 1000 millimeters
        scene.unit_settings.use_separate = True  # Display units in millimeters
    elif units == "METERS":
        scene.unit_settings.scale_length = 1.0  # Default for metric is meters
        scene.unit_settings.use_separate = False  # Display units in meters
    elif units == "CENTIMETERS":
        scene.unit_settings.scale_length = 0.01  # 1 meter = 100 centimeters
        scene.unit_settings.use_separate = True  # Display units in centimeters
    else:
        raise ValueError(f"Unsupported unit: {units}. Please use 'MILLIMETERS', 'CENTIMETERS', or 'METERS'.")