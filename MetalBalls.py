# Give Python access to Blender functionality
import bpy

# math for sine functions
import math

grid_size = 200
off_center = 2
scale = 0.125
z_scale = 4

# Adding the sphere
def create_sphere():
    bpy.ops.mesh.primitive_uv_sphere_add()
    bpy.ops.object.shade_smooth()
    return bpy.context.active_object

current_sphere = create_sphere()

# Positioning the sphere in the correct location
for x in range(0,grid_size):
    for y in range(0,grid_size):
        copy_sphere = current_sphere.copy()
        copy_sphere.location = (x*off_center,y*off_center, (math.sin(scale*y) + math.cos(scale*x))*z_scale)
        bpy.context.collection.objects.link(copy_sphere)
    