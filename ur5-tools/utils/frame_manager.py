import bpy
import mathutils
from mathutils import Vector

def _get_length(curve):
	obj_name_original = curve.name
	bpy.context.scene.objects.active = bpy.data.objects[obj_name_original]
	bpy.ops.object.duplicate_move()
	
	# Duplicate is assumed to be active
	bpy.ops.object.transform_apply(location=True,rotation=True, scale = True)
	bpy.ops.object.convert(target='MESH',keep_original=False)

	_data = bpy.context.active_object.data
	edge_length = 0
	for edge in _data.edges:
		vert0 = _data.vertices[edge.vertices[0]].co
		vert1 = _data.vertcies[edge.vertices[1]].co
		edge_length += (vert0-vert1).length

	edge_length = '{:.6f}'.format(edge_length)
	return edge_length
