# Blender Automated Rendering Framework

A modular Python framework for automating rendering tasks in Blender, allowing for efficient scene setup, material assignment, camera and lighting configuration, and batch rendering with customizable settings.

## Table of Contents

- Introduction
- Features
- Getting Started
  - Prerequisites
  - Installation
- Usage
  - Configuration File
  - Running the Script
- Project Structure


## Introduction

This project provides a flexible and extensible framework for automating rendering tasks in Blender using Python scripts. It leverages Blender's Python API to set up scenes, assign materials, configure cameras and lighting, and perform batch rendering based on customizable configuration files.

## Features

- **Modular Design**: Organized into modules for easy maintenance and extension.
- **Configuration-Driven**: Uses configuration files to specify scene parameters, allowing for quick adjustments without modifying code.
- **Material Assignment**: Automatically assigns materials to objects or meshes based on predefined properties stored in tissue_data.
- **Camera Setup**: Configures camera settings, including sensor size, focal length, and depth of field.
- **Lighting Configuration**: Supports various light types, positions, energies, colors, and shadow casting options.
- **Render Engine Initialization**: Sets up rendering parameters for Cycles or EEVEE, including sampling, denoising, and light paths.
- **Batch Rendering**: Processes multiple frames or scenes using specified transforms.json files or animations.
- **Error Handling and Logging**: Provides informative messages and handles common errors gracefully.

## Getting Started

### Prerequisites

- **Blender 3.x or 4.x**: Ensure you have Blender installed on your system. The scripts are compatible with Blender's Python API.
- **Python 3.x**: While Blender comes with its own Python interpreter, you may need Python 3.x for additional scripting or setup tasks.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/drichter-official/blender_sim_v2.git
   ```
   
2. **Navigate to the Project Directory**:

   ```bash
   cd blender_sim_v2
   ```


3. **Prepare and activate the Environment using Conda**:
    
   ```bash
   conda env create -f environment.yml
   conda activate blender_sim_v2
   ```

## Usage
### Configuration File

The framework uses a configuration file (e.g., config.ini) to define scene parameters. The configuration file is divided into sections, such as [Paths], [Camera], [Lighting], [RenderEngine], [LightPaths], etc.

### Running the Script

To execute the rendering script using a predefined config file, use the following command:

```
 python run.py --config_path configs/config_default.ini --load_config True
```

Otherwise you may use arguments to run the script with 

## Project Structure

```
blender-sim-v2/
├── run.py
├── configs/
│   └── config.ini
├── utils/
│   ├── camera_setup.py
│   ├── config_loader.py
│   ├── engine_utils.py
│   ├── material_setup.py
│   ├── scene_setup.py
│   ├── transform_loader.py
├── data/
│   ├── tissue_data.py         # Contains tissue materials and properties
│   └── input/
│       └── your_model.obj
├── output/
└── README.md
```


