import bpy

"""
In most cases, we want the Elbow mesh to be pointing semi-downwards in the -z direction. 

In general, the Elbow Mesh, Shoulder mesh and the table would make a "triangle"

Extended to other meshes/bones

Returns if the direcftion of the Elbow mesh is right
"""

def direction_vector(start_bone, end_bone):
	'''
	Returns the vector from the head of the start_bone to the tail of the end_bone
	'''
	start = start_bone.head
	end = end_bone.tail

	return end-start

def check_elbow_direction():
	'''
	Returns if the elbow has a negative z direction
	'''
	start_bone = obj.data.objects['Armature'].pose.bones['Shoulder']
	end_bone = obj.data.objects['Armature'].pose.bones['Elbow']
	vector = direction_vector(start_bone, end_bone)
	return vector.z < 0

def check_wrist2_direction(direction = 1):
	"""
	Returns if the wrist2 is in given direction
	
	Direction defaults to upwards
	"""

	bone = obj.data.objects['Armature'].pose.bones['Wrist2']
	if(direction > 0):
		return direction_vector(bone,bone) < 0
	else:
		return direction_vector(bone,bone) > 0