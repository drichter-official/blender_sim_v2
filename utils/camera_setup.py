# utils/camera_setup.py

import bpy
from mathutils import Matrix

def setup_camera(config):
    """
    Sets up the camera in the scene using Blender's camera_add operator.

    Parameters:
    - config: A dictionary containing camera settings.
    """
    # Extract camera parameters from the config
    location = config.get('camera_position', [0, 0, 0])
    rotation_euler = config.get('camera_rotation_euler', [1, 0, 0])
    focal_length = config.get('camera_focal_length', 40)
    sensor_size = config.get('camera_sensor_size', 36)
    depth_of_field = config.get('camera_depth_of_field', False)
    dof_focus_distance = config.get('camera_dof_focus_distance', 10.0)
    dof_aperture_fstop = config.get('camera_dof_aperture_fstop', 2.8)

    # Check if a camera named "Camera" already exists
    camera = bpy.data.objects.get("Camera")
    if camera is None:
        # Add a new camera using the operator
        bpy.ops.object.camera_add(location=location, rotation=rotation_euler)
        camera = bpy.context.object
        camera.name = "Camera"
    else:
        # Reuse the existing camera
        camera.location = location
        camera.rotation_euler = rotation_euler

    # Set camera properties
    camera.data.lens = focal_length
    camera.data.sensor_width = sensor_size

    # Depth of Field settings
    if depth_of_field:
        camera.data.dof.use_dof = True
        camera.data.dof.focus_distance = dof_focus_distance
        camera.data.dof.aperture_fstop = dof_aperture_fstop
    else:
        camera.data.dof.use_dof = False

    # Set the camera as the active camera
    bpy.context.scene.camera = camera

    print(f"Using camera: {camera.name}")
    return camera

def set_camera_extrinsic(camera, extrinsic_matrix):
    mat = Matrix(extrinsic_matrix)
    camera.location = mat.to_translation()
    camera.rotation_euler = mat.to_euler()