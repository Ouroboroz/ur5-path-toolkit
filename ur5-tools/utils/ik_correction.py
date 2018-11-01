import bpy
import bottom_limit_check, direction_check, mesh_intersect

"""
Runner script to correct ik contraints to fix the issues brought up by the checks
"""

def set_ik_contraints(bone, axis = 'y', min, max):
	"""
	Sets the ik_contraints for the input bone on the input axis. 

	The axis will default to 'y' since that is the rotation axis for bones in the UR5
	"""
	