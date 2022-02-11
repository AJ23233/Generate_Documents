# Filename: document_ops.py
# Description: This file manages all the operations that needs to be perform
# Author: Ajay Vanara

from importlib import import_module

class OperationManager:
	
	def __init__(self):
		pass

	def execute_operation(self, ops_name, method=None, params=None):
		"""
		Method to manage all the operations that needs to be performed 
		"""
		try:
			import pdb; pdb.set_trace
			op = ops_name +'_ops'
			cls = getattr(import_module(".".join(["Operations",op])),
										"".join([o.capitalize() for o in op.split("_")]))

			if method:
				method = getattr(cls(), method)
				if params:
					if isinstance(params, str):
						result = method(params)
					else:
						result = method(*params)
				else:
					result = method()
			else:
				result = cls

		except Exception as ex:
			print("Error while managing the operations :{}".format(str(ex)))
			
		return result


