# utils/config_loader.py

import argparse
import configparser

def load_config(argv):
    parser = argparse.ArgumentParser(description='Process rendering configurations.')

    # Define command-line arguments
    parser.add_argument('--config_path', type=str, default='./data/configs/config_normal.ini')
    parser.add_argument('--load_config', action='store_true')

    # Parse known arguments
    args, remaining_argv = parser.parse_known_args(argv[1:])

    # Load configuration file if specified
    config = configparser.ConfigParser()
    if args.load_config:
        print('Loading configuration from file')
        config.read(args.config_path)

    # Initialize args dictionary
    config_dict = {}

    # Individually initialize each configuration argument
    # Paths
    config_dict['object_file_path'] = get_config_value(
        config, 'Paths', 'object_file_path', default='./data/input/reference.obj'
    )
    config_dict['transforms_file_path'] = get_config_value(
        config, 'Paths', 'transforms_file_path', default=None
    )
    config_dict['output_directory'] = get_config_value(
        config, 'Paths', 'output_directory', default='./output'
    )

    # Camera settings
    config_dict['camera_position'] = parse_float_list(
        get_config_value(config, 'Camera', 'camera_position', default='0,0,0')
    )
    config_dict['camera_rotation_euler'] = parse_float_list(
        get_config_value(config, 'Camera', 'camera_rotation_euler', default='0,0,0')
    )
    config_dict['camera_focal_length'] = float(
        get_config_value(config, 'Camera', 'camera_focal_length', default=12)
    )
    config_dict['camera_sensor_size'] = float(
        get_config_value(config, 'Camera', 'camera_sensor_size', default=3.726)
    )
    config_dict['camera_resolution'] = parse_int_list(
        get_config_value(config, 'Camera', 'camera_resolution', default='800,800')
    )
    config_dict['camera_clip_start'] = float(
        get_config_value(config, 'Camera', 'camera_clip_start', default=0.1)
    )
    config_dict['camera_clip_end'] = float(
        get_config_value(config, 'Camera', 'camera_clip_end', default=1000.0)
    )
    config_dict['camera_background_color'] = parse_float_list(
        get_config_value(config, 'Camera', 'camera_background_color', default='0,0,0,0')
    )
    config_dict['camera_use_transparent_background'] = config.getboolean(
        'Camera', 'camera_use_transparent_background', fallback=False
    )
    config_dict['camera_depth_of_field'] = config.getboolean(
        'Camera', 'camera_depth_of_field', fallback=False
    )
    config_dict['camera_dof_focus_distance'] = float(
        get_config_value(config, 'Camera', 'camera_dof_focus_distance', default=10.0)
    )
    config_dict['camera_dof_aperture_fstop'] = float(
        get_config_value(config, 'Camera', 'camera_dof_aperture_fstop', default=2.8)
    )

    # Render engine settings
    config_dict['render_engine'] = get_config_value(
        config, 'RenderEngine', 'render_engine', default='CYCLES'
    )
    config_dict['render_samples'] = int(
        get_config_value(config, 'RenderEngine', 'render_samples', default=128)
    )
    config_dict['render_use_adaptive_sampling'] = config.getboolean(
        'RenderEngine', 'render_use_adaptive_sampling', fallback=False
    )
    config_dict['render_adaptive_threshold'] = float(
        get_config_value(config, 'RenderEngine', 'render_adaptive_threshold', default=0.01)
    )
    config_dict['render_use_denoising'] = config.getboolean(
        'RenderEngine', 'render_use_denoising', fallback=False
    )
    config_dict['render_denoising_strength'] = float(
        get_config_value(config, 'RenderEngine', 'render_denoising_strength', default=0.5)
    )
    config_dict['render_denoising_prefilter'] = get_config_value(
        config, 'RenderEngine', 'render_denoising_prefilter', default='ACCURATE'
    )

    # Light path settings
    config_dict['max_bounces_total'] = int(
        get_config_value(config, 'LightPaths', 'max_bounces_total', default=12)
    )
    config_dict['max_bounces_diffuse'] = int(
        get_config_value(config, 'LightPaths', 'max_bounces_diffuse', default=4)
    )
    config_dict['max_bounces_glossy'] = int(
        get_config_value(config, 'LightPaths', 'max_bounces_glossy', default=4)
    )
    config_dict['max_bounces_transmission'] = int(
        get_config_value(config, 'LightPaths', 'max_bounces_transmission', default=12)
    )
    config_dict['max_bounces_volume'] = int(
        get_config_value(config, 'LightPaths', 'max_bounces_volume', default=0)
    )
    config_dict['max_bounces_transparent'] = int(
        get_config_value(config, 'LightPaths', 'max_bounces_transparent', default=12)
    )
    config_dict['caustics_reflective'] = config.getboolean(
        'LightPaths', 'caustics_reflective', fallback=False
    )
    config_dict['caustics_refractive'] = config.getboolean(
        'LightPaths', 'caustics_refractive', fallback=False
    )

    # Object settings
    config_dict['object_rotation_degrees'] = float(
        get_config_value(config, 'Object', 'object_rotation_degrees', default=0)
    )
    config_dict['object_rotation_axis'] = get_config_value(
        config, 'Object', 'object_rotation_axis', default='Y'
    )
    config_dict['object_scale'] = float(
        get_config_value(config, 'Object', 'object_scale', default=1)
    )
    config_dict['object_diffuse_color_rgba'] = parse_float_list(
        get_config_value(config, 'Object', 'object_diffuse_color_rgba', default='1,1,1,1')
    )

    # Lighting settings
    config_dict['light_setting'] = get_config_value(
        config, 'Lighting', 'light_setting', default='external'
    )
    config_dict['light_positions'] = parse_list_of_float_tuples(
        get_config_value(config, 'Lighting', 'light_positions', default=None)
    )
    config_dict['light_types'] = get_config_value(
        config, 'Lighting', 'light_types', default='POINT'
    ).split(',')
    config_dict['light_radii'] = parse_float_list(
        get_config_value(config, 'Lighting', 'light_radii', default='2')
    )
    config_dict['light_energies'] = parse_float_list(
        get_config_value(config, 'Lighting', 'light_energies', default='100000')
    )
    config_dict['light_colors'] = parse_list_of_float_tuples(
        get_config_value(config, 'Lighting', 'light_colors', default='1,1,1')
    )
    config_dict['light_cast_shadows'] = parse_boolean_list(
        get_config_value(config, 'Lighting', 'light_cast_shadows', default='True')
    )

    # Environment settings
    config_dict['environment_texture_path'] = get_config_value(
        config, 'Environment', 'environment_texture_path', default=None
    )
    config_dict['environment_strength'] = float(
        get_config_value(config, 'Environment', 'environment_strength', default=1.0)
    )
    config_dict['environment_rotation'] = float(
        get_config_value(config, 'Environment', 'environment_rotation', default=0.0)
    )

    # Output settings
    config_dict['output_file_prefix'] = get_config_value(
        config, 'Output', 'output_file_prefix', default='render_'
    )
    config_dict['output_image_format'] = get_config_value(
        config, 'Output', 'output_image_format', default='PNG'
    )
    config_dict['output_color_mode'] = get_config_value(
        config, 'Output', 'output_color_mode', default='RGBA'
    )
    config_dict['output_color_depth'] = int(
        get_config_value(config, 'Output', 'output_color_depth', default=8)
    )
    config_dict['output_compression'] = int(
        get_config_value(config, 'Output', 'output_compression', default=15)
    )
    config_dict['output_overwrite'] = config.getboolean(
        'Output', 'output_overwrite', fallback=True
    )

    # Scene settings
    config_dict['scene_units'] = get_config_value(
        config, 'Scene', 'scene_units', default='METERS'
    )
    config_dict['scene_gravity'] = parse_float_list(
        get_config_value(config, 'Scene', 'scene_gravity', default='0,0,0')
    )
    config_dict['scene_frame_start'] = int(
        get_config_value(config, 'Scene', 'scene_frame_start', default=1)
    )
    config_dict['scene_frame_end'] = int(
        get_config_value(config, 'Scene', 'scene_frame_end', default=250)
    )
    config_dict['scene_frame_step'] = int(
        get_config_value(config, 'Scene', 'scene_frame_step', default=1)
    )

    # Advanced settings
    config_dict['use_gpu_rendering'] = config.getboolean(
        'Advanced', 'use_gpu_rendering', fallback=False
    )
    config_dict['gpu_device_type'] = get_config_value(
        config, 'Advanced', 'gpu_device_type', default='CUDA'
    )
    config_dict['render_tile_size'] = int(
        get_config_value(config, 'Advanced', 'render_tile_size', default=256)
    )
    config_dict['film_exposure'] = float(
        get_config_value(config, 'Advanced', 'film_exposure', default=1.0)
    )
    config_dict['film_transparent'] = config.getboolean(
        'Advanced', 'film_transparent', fallback=True
    )

    # Debugging settings
    config_dict['verbose_logging'] = config.getboolean(
        'Debug', 'verbose_logging', fallback=False
    )
    config_dict['log_file_path'] = get_config_value(
        config, 'Debug', 'log_file_path', default='./logs/render.log'
    )

    return config_dict

def get_config_value(config, section, option, default=None):
    if config.has_option(section, option):
        return config.get(section, option)
    else:
        return default

def parse_float_list(value):
    return [float(x.strip()) for x in value.split(',')]

def parse_int_list(value):
    return [int(x.strip()) for x in value.split(',')]

def parse_list_of_float_tuples(value):
    if not value:
        return None
    tuples = value.split(';')
    return [tuple(map(float, t.strip().split(','))) for t in tuples]

def parse_boolean_list(value):
    return [x.strip().lower() in ('true', '1', 'yes') for x in value.split(',')]