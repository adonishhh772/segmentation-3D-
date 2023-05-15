'''
Prepares Blender for manual segmentation of 4 classes
Requires Blender 2.8
Author: Lisa Schneider

@input:
    Object with 4 segmentation classes

@output:
    Blender is prepared with 4 vertex groups and assigned colors
'''
import bpy
bpy.ops.object.mode_set(mode='EDIT')
group = bpy.context.object.vertex_groups.new(name="1")
group = bpy.context.object.vertex_groups.new(name="2")


#Assign material to vertex group
red = bpy.data.materials.new(name='red')
bpy.context.object.data.materials.append(red)
yellow = bpy.data.materials.new(name='yellow')



bpy.data.materials['red'].diffuse_color = (0.938686, 0.0069953, 0.0122865, 1)
bpy.data.materials['yellow'].diffuse_color = (1, 0.346704, 0.0116123, 1)


bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.object.vertex_group_deselect()

for i in range(1,3):
 bpy.ops.object.vertex_group_set_active(group=str(i))
 bpy.ops.object.vertex_group_select()
 bpy.context.object.active_material_index = i
 bpy.ops.object.material_slot_assign()
 bpy.ops.object.vertex_group_deselect()