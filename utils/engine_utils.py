# render_engine_utils.py

import bpy
def initialize_engine(config):
    """
    Initializes the render engine settings based on the provided configuration.

    Parameters:
    - config: A dictionary containing render engine settings.

    Supported Configurations:
    - Render Engine Settings
    - Sampling Settings
    - Denoising Settings
    - Light Path Settings (specific to Cycles)
    """
    scene = bpy.context.scene

    # Set render engine
    render_engine = config.get('render_engine', 'CYCLES')
    scene.render.engine = render_engine

    # Common render settings
    scene.render.image_settings.file_format = config.get('render_file_format', 'PNG')
    scene.render.image_settings.color_depth = str(config.get('render_color_depth', 8))
    scene.render.use_motion_blur = config.get('render_use_motion_blur', False)
    if scene.render.use_motion_blur:
        scene.render.motion_blur_shutter = config.get('render_motion_blur_shutter', 0.5)

    # Engine-specific settings
    if render_engine == 'CYCLES':
        cycles = scene.cycles

        # Device settings
        if config.get('use_gpu_rendering', False):
            cycles.device = 'GPU'
            bpy.context.preferences.addons['cycles'].preferences.compute_device_type = config.get('gpu_device_type', 'CUDA')
            bpy.context.preferences.addons['cycles'].preferences.get_devices()
            for device in bpy.context.preferences.addons['cycles'].preferences.devices:
                device.use = True
        else:
            cycles.device = 'CPU'

        # Sampling
        cycles.samples = config.get('render_samples', 128)
        cycles.use_adaptive_sampling = config.get('render_use_adaptive_sampling', False)
        if cycles.use_adaptive_sampling:
            cycles.adaptive_threshold = config.get('render_adaptive_threshold', 0.01)

        # Denoising
        cycles.use_denoising = config.get('render_use_denoising', False)
        if cycles.use_denoising:
            cycles.denoiser = 'OPTIX'  # Options: 'NLM', 'OPTIX', 'OPENIMAGEDENOISE'
            # Note: Adjusting denoising strength and prefilter may require compositor nodes

        # Light Path Settings
        cycles.max_bounces = config.get('max_bounces_total', 12)
        cycles.diffuse_bounces = config.get('max_bounces_diffuse', 4)
        cycles.glossy_bounces = config.get('max_bounces_glossy', 4)
        cycles.transmission_bounces = config.get('max_bounces_transmission', 12)
        cycles.volume_bounces = config.get('max_bounces_volume', 0)
        cycles.transparent_max_bounces = config.get('max_bounces_transparent', 12)
        cycles.caustics_reflective = config.get('caustics_reflective', False)
        cycles.caustics_refractive = config.get('caustics_refractive', False)

        # Additional Cycles settings can be added here

    elif render_engine == 'BLENDER_EEVEE':
        eevee = scene.eevee

        # Sampling
        eevee.taa_render_samples = config.get('render_samples', 64)

        # Note: EEVEE does not support the same Light Path settings as Cycles

    else:
        print(f"Unsupported render engine: {render_engine}")

    # Output settings
    scene.render.image_settings.file_format = config.get('render_file_format', 'PNG')
    scene.render.image_settings.color_depth = str(config.get('render_color_depth', 8))

    # Film settings
    scene.render.film_transparent = config.get('film_transparent', False)

    # Color management and exposure
    scene.view_settings.exposure = config.get('film_exposure', 1.0)

def render_image(output_path,config):
    resolution = config.get('camera_resolution', [None, None])

    scene = bpy.context.scene
    scene.render.image_settings.file_format = config.get('output_image_format')
    scene.render.filepath = output_path
    scene.render.resolution_x = resolution[0]
    scene.render.resolution_y = resolution[1]
    bpy.ops.render.render(write_still=True)
