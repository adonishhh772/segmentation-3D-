
import bpy
import numpy as np

'''
Extracts edge labels from segmentation via Blender 
Requires Blender 2.8
Author: Lisa Schneider

@input: 
    Segmented object in Blender

@output:
    .txt file with labels per edge
    to run it insert into Blender console after segmenting the object
'''

verticeGroups = {}
edgeLabels = []
faceLabels = []
edges = []
faces_edges = []
edge_nb = []
edge2key = {}
edges_count = 0
nb_count = []
eseg_path = 'C:/Users/AbdBastola/Documents/Custom Segmentation/seg/cus/{}.npz'

ob = bpy.context.object
obdata = bpy.context.object.data

vgroup_names = {vgroup.index: vgroup.name for vgroup in ob.vertex_groups}
vgroups = {v.index: [vgroup_names[g.group] for g in v.groups] for v in obdata.vertices}

#get group for vertices; save in dict
for idx in range(len(obdata.vertices)):
    group = vgroups[idx]
    verticeGroups[idx] = group

#each edge made of two vertices; get group of first vertice
for idx, edge in enumerate(vgroups):
    groups = verticeGroups[idx]
    if len(groups) != 0:
        if len(groups) == 2:
            edgeLabels.append(int(groups[1]))
        else:
            edgeLabels.append(int(groups[0]))
    else:
        edgeLabels.append(0)
         
#print(edgeLabels)

np.savez_compressed(eseg_path.format(bpy.context.active_object.name), edgeLabels)

