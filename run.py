# run.py

import os
import sys

import bpy

from data.tissue_data import (tissue_list,
                              tissue_properties,
                              meshes)
from utils.camera_setup import (setup_camera,
                                set_camera_extrinsic)
from utils.config_loader import load_config
from utils.engine_utils import (initialize_engine,
                                render_image)
from utils.material_setup import (create_tissue_materials,
                                  assign_materials_to_meshes)
from utils.scene_setup import (clear_scene,
                               set_transparent_background,
                               setup_lights,
                               load_object,
                               set_scene_units)
from utils.transform_loader import load_transforms


def main():
    # Load the configuration from the command-line arguments
    config = load_config(sys.argv)

    # Reset Blender to its default state, removing all objects and settings
    bpy.ops.wm.read_factory_settings(use_empty=True)
    clear_scene()  # Clear any remaining objects from the scene

    # Create the output directory if it doesn't exist
    if not os.path.exists(config['output_directory']):
        os.makedirs(config['output_directory'])
    print(config)  # Print the configuration to verify settings

    # Load transformation data from the specified file
    transforms = load_transforms(config['transforms_file_path'])

    # Set a transparent background if specified in the configuration
    if config.get('camera_use_transparent_background', False):
        set_transparent_background()

    # Set up the lighting in the scene based on the configuration
    setup_lights(config)

    # Load the 3D object into the scene from the specified file and apply euler transformations
    load_object(config)

    # Create and assign materials to the tissues based on predefined properties
    create_tissue_materials(config,tissue_list, tissue_properties)
    assign_materials_to_meshes(meshes)

    # Set up the camera based on the configuration settings
    camera = setup_camera(config)

    # Initialize the rendering engine with the given configuration
    initialize_engine(config)

    # Enable transparent background again, just in case it wasn't set earlier
    if config.get('camera_use_transparent_background', False):
        set_transparent_background()

    # Set the units of the scene (e.g., metric or imperial) based on configuration
    set_scene_units(config)

    # Iterate through each frame transformation and render the image
    for frame in transforms['frames']:
        # Set the camera extrinsic parameters (position and orientation) for each frame
        transform_matrix = frame['transform_matrix']
        set_camera_extrinsic(camera, transform_matrix)

        # Define the output path for the rendered image
        output_path = os.path.join(config['output_directory'], frame['file_path'])

        # Render the image and save it to the specified output path
        render_image(output_path, config)


# Run the main function when the script is executed
if __name__ == '__main__':
    main()
