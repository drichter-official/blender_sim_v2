# utils/argparse_config.py

import argparse
import configparser

def load_config(argv):
    parser = argparse.ArgumentParser(description='Process rendering configurations.')

    # Paths
    parser.add_argument('--object_file_path', type=str, default='./data/input/reference.obj')
    parser.add_argument('--transforms_file_path', type=str)
    parser.add_argument('--output_directory', type=str)

    # Camera settings
    parser.add_argument('--camera_position', type=float, nargs=3, default=[0, 0, 0])
    parser.add_argument('--camera_rotation_euler', type=float, nargs=3, default=[0, 0, 1])
    parser.add_argument('--camera_focal_length', type=float, default=12)
    parser.add_argument('--camera_sensor_size', type=float, default=3.726)
    parser.add_argument('--camera_resolution', type=int, nargs=2, default=[800, 800])
    parser.add_argument('--camera_clip_start', type=float, default=0.1)
    parser.add_argument('--camera_clip_end', type=float, default=1000.0)
    parser.add_argument('--camera_background_color', type=float, nargs=4, default=[0, 0, 0, 0])
    parser.add_argument('--camera_use_transparent_background', action='store_true')
    parser.add_argument('--camera_depth_of_field', action='store_true')
    parser.add_argument('--camera_dof_focus_distance', type=float, default=10.0)
    parser.add_argument('--camera_dof_aperture_fstop', type=float, default=2.8)

    # Render engine settings
    parser.add_argument('--render_engine', type=str, default='CYCLES')
    parser.add_argument('--render_samples', type=int, default=128)
    parser.add_argument('--render_use_adaptive_sampling', action='store_true')
    parser.add_argument('--render_adaptive_threshold', type=float, default=0.01)
    parser.add_argument('--render_use_denoising', action='store_true')
    parser.add_argument('--render_denoising_strength', type=float, default=0.5)
    parser.add_argument('--render_denoising_prefilter', type=str, default='ACCURATE')
    parser.add_argument('--render_file_format', type=str, default='PNG')
    parser.add_argument('--render_color_depth', type=int, default=8)
    parser.add_argument('--render_use_motion_blur', action='store_true')
    parser.add_argument('--render_motion_blur_shutter', type=float, default=0.5)

    # Light path settings (specific to Cycles)
    parser.add_argument('--max_bounces_total', type=int, default=12)
    parser.add_argument('--max_bounces_diffuse', type=int, default=4)
    parser.add_argument('--max_bounces_glossy', type=int, default=4)
    parser.add_argument('--max_bounces_transmission', type=int, default=12)
    parser.add_argument('--max_bounces_volume', type=int, default=4)
    parser.add_argument('--max_bounces_transparent', type=int, default=12)
    parser.add_argument('--caustics_reflective', action='store_true')
    parser.add_argument('--caustics_refractive', action='store_true')

    # Object settings
    parser.add_argument('--object_rotation_degrees', type=float, default=0)
    parser.add_argument('--object_rotation_axis', type=str, default='Y')
    parser.add_argument('--object_scale', type=float, default=1)
    parser.add_argument('--object_material', type=str, default='default_material')
    parser.add_argument('--object_use_smooth_shading', action='store_true')
    parser.add_argument('--object_diffuse_color_rgba', type=float, nargs=4, default=[1, 1, 1, 1])
    parser.add_argument('--object_specular_intensity', type=float, default=0.5)
    parser.add_argument('--object_roughness', type=float, default=0.5)

    # Lighting settings
    parser.add_argument('--light_positions', type=str, default=None)
    parser.add_argument('--light_types', type=str, default='POINT')
    parser.add_argument('--light_radii', type=str, default='2')
    parser.add_argument('--light_energies', type=str, default='100000')
    parser.add_argument('--light_colors', type=str, default='1,1,1')
    parser.add_argument('--use_diffusive_light', action='store_true')
    parser.add_argument('--diffusive_light_color_rgba', type=float, nargs=4, default=[1, 1, 1, 1])

    # Environment settings
    parser.add_argument('--environment_texture_path', type=str, default=None)
    parser.add_argument('--environment_strength', type=float, default=1.0)
    parser.add_argument('--environment_rotation', type=float, default=0.0)

    # Output settings
    parser.add_argument('--output_image_format', type=str, default='PNG')
    parser.add_argument('--output_color_mode', type=str, default='RGBA')
    parser.add_argument('--output_color_depth', type=int, default=8)
    parser.add_argument('--output_compression', type=int, default=15)
    parser.add_argument('--output_overwrite', action='store_true')

    # Scene settings
    parser.add_argument('--scene_units', type=str, default='METERS')
    parser.add_argument('--scene_gravity', type=float, nargs=3, default=[0, 0, 0])
    parser.add_argument('--scene_frame_start', type=int, default=1)
    parser.add_argument('--scene_frame_end', type=int, default=250)
    parser.add_argument('--scene_frame_step', type=int, default=1)

    # Advanced rendering settings
    parser.add_argument('--use_gpu_rendering', action='store_true')
    parser.add_argument('--gpu_device_type', type=str, default='CUDA')
    parser.add_argument('--render_tile_size', type=int, default=256)
    parser.add_argument('--film_exposure', type=float, default=1.0)
    parser.add_argument('--film_transparent', action='store_true')

    # Debugging settings
    parser.add_argument('--verbose_logging', action='store_true')
    parser.add_argument('--log_file_path', type=str, default='./logs/render.log')

    # Configuration file
    parser.add_argument('--config_path', type=str, default='./configs/config_normal.ini')
    parser.add_argument('--load_config', action='store_true')

    args, unknown = parser.parse_known_args(argv[1:])

    # Load configuration file if specified
    config = configparser.ConfigParser()
    if args.load_config:
        print(f"Loading config from {args.config_path}")
        config.read(args.config_path)
        config_dict = {key: value for section in config.sections() for key, value in config[section].items()}
    else:
        config_dict = vars(args)
    return config_dict

def eval_value(value):
    try:
        # Try to evaluate the value as a Python literal
        return eval(value)
    except:
        return value