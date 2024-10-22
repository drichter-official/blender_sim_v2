# material_utils.py

import bpy

def create_tissue_materials(tissue_list, tissue_properties):
    """
    Creates materials for each tissue type based on provided properties.
    """
    for tissue in tissue_list:
        # Create a new material
        mat = bpy.data.materials.new(name=tissue)
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links

        # Clear default nodes
        nodes.clear()

        # Add Principled BSDF node
        principled_bsdf = nodes.new(type="ShaderNodeBsdfPrincipled")
        principled_bsdf = nodes.new(type="ShaderNodeBsdfTranslucent")
        principled_bsdf.location = (0, 0)

        # Set Base Color (customize as needed)
        #principled_bsdf.inputs["Base Color"].default_value = (1.0, 1.0, 1.0, 1.0)

        # Set properties from tissue_properties
        #principled_bsdf.inputs["IOR"].default_value = tissue_properties[tissue]["refractive_index"]
        #principled_bsdf.inputs["Alpha"].default_value = 1
        #principled_bsdf.inputs["Transmission Weight"].default_value = 1
        if tissue == "TUMOR":
            pass
            #principled_bsdf.inputs["Emission Strength"].default_value = tissue_properties[tissue]["emission"]
        # Note: Subsurface Anisotropy is not directly available; use Subsurface Scattering if needed
        #principled_bsdf.inputs["Subsurface Weight"].default_value = 0.5
        #principled_bsdf.inputs["Subsurface Anisotropy"].default_value = tissue_properties[tissue]["anisotropy"]

        # Add Volume Scatter node
        #volume_scatter = nodes.new(type="ShaderNodeVolumeScatter")
        #volume_scatter.location = (0, -400)
        #volume_scatter.inputs["Density"].default_value = tissue_properties[tissue]["density"]
        #volume_scatter.inputs["Anisotropy"].default_value = tissue_properties[tissue]["anisotropy"]

        volume_absorption = nodes.new(type="ShaderNodeVolumeAbsorption")
        volume_absorption.location = (0, -400)
        volume_absorption.inputs["Density"].default_value = tissue_properties[tissue]["density"]

        # Add Material Output node
        output_node = nodes.new(type="ShaderNodeOutputMaterial")
        output_node.location = (400, 0)

        # Link nodes
        links.new(principled_bsdf.outputs["BSDF"], output_node.inputs["Surface"])
        #links.new(volume_scatter.outputs["Volume"], output_node.inputs["Volume"])
        links.new(volume_absorption.outputs["Volume"], output_node.inputs["Volume"])
def assign_materials_to_meshes(meshes):
    """
    Assigns materials to meshes based on a mapping of mesh names to tissue names.
    """

    for obj_name, tissue_name in meshes.items():
        # Find the object by name
        obj = bpy.data.objects.get(obj_name)
        if obj is not None and obj.type == 'MESH':
            # Get the material
            mat = bpy.data.materials.get(tissue_name)
            if mat is not None:
                # Assign the material to the object
                if obj.data.materials:
                    # Replace the existing material
                    obj.data.materials[0] = mat
                else:
                    # Add the material to the object
                    obj.data.materials.append(mat)
                print(f"Assigned material {tissue_name} to mesh {obj_name}")
            else:
                print(f"Material '{tissue_name}' not found.")
        else:
            print(f"Object '{obj_name}' not found.")