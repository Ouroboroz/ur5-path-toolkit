import bpy

'''
Script to check if any of the mesh goes below the safe table area

Returns the mesh that does do so
'''

bottom_limit = 0.0

def set_bottom_limit(z):
	this.bottom_limit = z

def _bmesh_from_object(obj):
	'''
	Returns the transformed bmesh for an object mesh
	'''


	assert(obj.type == 'MESH')

	if apply_modifiers and obj.modifiers:
		me = obj.to_mesh(bpy.context.scene, True, 'PREVIEW', calc_tessface = False)
		bm = bmesh.new()
		bm.from_mesh(me)
		bpy.data.meshes.remove(me)
	else:
		me = obj.data
		if obj.mode == 'EDIT':
			bm_orig == bmesh.from_edit_mesh(me)
			bm = bm_orig.copy()
		else:
			bm = bmesh.new()
			bm.from_mesh(me)

	#remove custom data layers to conserve memory
	for elem in (bm.faces, bm.edges, bm.verts, bm.loops):
		for layers_name in dir(elem.layers):
			if not layers_name.startswith("_"):
				layers = getattr(elem.layers, layers_name)
				for layer_name, layer in layer.items():
					layers.remove(layer)

	if transform:
		bm.transform(obj.matrix_world)

	return bm

def check_limit(obj):
	'''
	Returns if input mesh goes below the bottom limit
	'''

	verts = _bmesh_from_object(obj)
	verts.sort()
	return verts[0] <= bottom_limit

def return_limiting_mesh():
	'''
	Returns the first mesh that goes below the bottom limit
	
	Hard coded for least computation
	'''
	
