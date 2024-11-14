# run_multi.py

import os
import subprocess

# Set the root directory to search
root_dir = "/home/daniel/projects/blender_sim_v2/configs/experiments/synthetic_generated_data"

# Recursively search for config.ini files and run the command
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('config.ini'):
            config_path = os.path.join(root, file)
            command = [
                "python", "run.py",
                "--config_path", config_path,
                "--load_config", "True"
            ]

            try:
                # Run the command
                subprocess.run(command, check=True)
                print(f"Successfully ran command for {config_path}")
            except subprocess.CalledProcessError as e:
                print(f"Error occurred while running command for {config_path}: {e}")
