import bpy
import bottom_limit_check, direction_check, mesh_intersect
import math
"""
Runner script to correct ik contraints to fix the issues brought up by the checks
"""

def _set_ik_contraints(bone, min, max, axis = 'y'):
	"""
	Sets the ik_contraints for the input bone on the input axis. 

	The axis will default to 'y' since that is the rotation axis for bones in the UR5
	"""

	if(axis == 'y'):
		bone.ik_min_y = min
		bone.ik_max_y = max
	else if(axis == 'x'):
		bone.ik_min_x = min
		bone.ik_max_x = max
	else if(axis == 'z'):
		bone.ik_min_z = min
		bone.ik_max_z = max
	#Refresh the contraints
	bpy.context.scene.update()

def _change_ik_contraints(bone, change_min, change_max , is_increase = True, axis = 'y'):
	"""
	Changes the ik contraints for the input bone on the input axis

	The axis will default to 'y' and the change will be assumed to positive
	"""
	if(axis = 'y'):
		bone.ik_min_y += (2*int(is_increase)-1)*change_min
		bone.ik_max_y += (2*int(is_increase)-1)*change_max
	if(axis = 'x'):
		bone.ik_min_x += (2*int(is_increase)-1)*change_min
		bone.ik_max_x += (2*int(is_increase)-1)*change_max
	if(axis = 'z'):
		bone.ik_min_z += (2*int(is_increase)-1)*change_min
		bone.ik_max_z += (2*int(is_increase)-1)*change_max
	#Refresh the contraints
	bpy.data.scene.update()
def fix_bottom_limit():
	"""
	Fixes the ik contraints of the shoulder to raise the armature over the safe table area

	As of now, it only changes the shoulder. If more limiting cases come up, more detailed change will be made
	"""
	while(bottom_limit_check.return_limiting_mesh() != None):
		_change_ik_contraints(bpy.data.objects['Armature'].pose.bones["Shoulder"],0.5/180*math.pi,0)
