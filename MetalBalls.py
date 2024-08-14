# Give Python access to Blender functionality
import bpy

# math for sine functions
import math

grid_size = 20

# Adding the sphere
def create_sphere(current_location):
    bpy.ops.mesh.primitive_uv_sphere_add(location = current_location)
    bpy.ops.object.shade_smooth()

# Positioning the sphere in the correct location
for x in range(0,grid_size):
    for y in range(0,grid_size):
        create_sphere(current_location = (x*2,y*2, math.sin(y) + math.cos(x))
    