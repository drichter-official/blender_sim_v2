import configparser
import os

# Define the path to the base config and output config directory
base_config_path = '/home/daniel/projects/blender_sim_v2/configs/config_default.ini'
# Load the base configuration from base_config.ini
config = configparser.ConfigParser()
config.read(base_config_path)

print("Loaded Base Configuration:")
for section in config.sections():
    print(f"[{section}]")
    for key, value in config[section].items():
        print(f"{key} = {value}")
    print()
objects = [ "./data/input/reference_digimouse_skin.obj", "./data/input/reference.obj"]
lights_setups_external = [("1_0,0,100","0,0,100",1),
                          ("2_0,0,100;0,0,-100", "0,0,100;0,0,-100", 2),
                          ("3_86.6,0,50;0,0,-100;-86.6,0,50", "86.6,0,50;0,0,-100;-86.6,0,50", 3),
                          ("4_0,0,100;100,0,0;-100,0,0;0,0,-100", "0,0,100;100,0,0;-100,0,0;0,0,-100", 4),
                          ("6_0,0,100;86.6,0,50;86.6,0,-50;0,0,-100;-86.6,0,-50;-86.6,0,50", "0,0,100;86.6,0,50;86.6,0,-50;0,0,-100;-86.6,0,-50;-86.6,0,50",6)]

lights_setups_internal = [("1_0,0,0","0,0,0",1),
                          ("1_0,20,0","0,20,0",1),
                          ("1_0,-20,0","0,-20,0",1),
                          ("2_0,20,0;0,-20,0","0,20,0;0,-20,0",2),
                          ("2_0,0,0;0,20,0","0,0,0;0,20,0",2),
                          ("2_0,0,0;0,-20,0","0,0,0;0,-20,0",2)]

light_strenghts = [500,1000,5000,10000,50000,100000]

transform_dirs_path = '/home/daniel/projects/PyFlowControl/data/synthetic_data'
for transform_dir in os.listdir(transform_dirs_path):
    config["Paths"]["transforms_file_path"] = transform_dirs_path + "/" + transform_dir +"/transforms.json"
    config["Lighting"]["light_setting"] = "external"
    for lights in lights_setups_external:
        name,pos,num = lights
        for strength in light_strenghts:
            config["Paths"]["output_directory"] = transform_dirs_path+"/" + transform_dir + '/external_' + name + '_' + str(strength)

            config["Lighting"]["light_positions"] = pos
            config["Lighting"]["light_types"] = ','.join(["POINT"] * num)
            config["Lighting"]["light_radii"] = ','.join(["1"] * num)
            config["Lighting"]["light_energies"] = ','.join([str(strength)] * num)
            config["Lighting"]["light_colors"] = ';'.join(["1,1,1"] * num)
            config["Lighting"]["light_cast_shadows"] = ','.join(["True"] * num)

            # Define the file path
            filepath = "/home/daniel/projects/blender_sim_v2/configs/experiments/synthetic_generated_data/"+transform_dir.replace("/","_") + '_external_' + name + '_' + str(strength) + "_config.ini"

            # Create the directory if it does not exist
            directory = os.path.dirname(filepath)
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Write the modified config to a new file
            with open(filepath, 'w') as configfile:
                config.write(configfile)

    config["Lighting"]["light_setting"] = "internal"
    for lights in lights_setups_internal:
        name, pos, num = lights
        for strength in light_strenghts:
            config["Paths"]["output_directory"] = transform_dirs_path+"/" + transform_dir + '/internal_' + name + '_' + str(strength)

            config["Lighting"]["light_positions"] = pos
            config["Lighting"]["light_types"] = ','.join(["POINT"] * num)
            config["Lighting"]["light_radii"] = ','.join(["1"] * num)
            config["Lighting"]["light_energies"] = ','.join([str(strength)] * num)
            config["Lighting"]["light_colors"] = ';'.join(["1,1,1"] * num)
            config["Lighting"]["light_cast_shadows"] = ','.join(["True"] * num)

            # Define the file path
            filepath = "/home/daniel/projects/blender_sim_v2/configs/experiments/synthetic_generated_data/"+transform_dir.replace("/","_") + '_internal_' + name + '_' + str(strength) + "_config.ini"

            # Create the directory if it does not exist
            directory = os.path.dirname(filepath)
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Write the modified config to a new file
            with open(filepath, 'w') as configfile:
                config.write(configfile)

            print(f"Created configuration file: {filepath}")