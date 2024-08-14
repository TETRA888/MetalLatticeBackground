# Give Python access to Blender functionality
import bpy

# math for sine functions
import math


# Adding the sphere
def create_sphere(current_location):
    bpy.ops.mesh.primitive_uv_sphere_add(location = current_location)
    bpy.ops.object.shade_smooth()

# Positioning the sphere in the correct location
for x in range(0,10):
    for y in range(0,10):
        create_sphere(current_location = (x*2,y*2, math.sin(x)))
    


