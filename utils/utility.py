# Filename: utility.py
# Description: This file contains all the operations that needs to be perform on the documents
# Author: Ajay Vanara

import pandas as pd
import os
import shutil
from Operations.Operation_manager import OperationManager

def generate_df(data):
	"""
	This method is used to generate dataframe 
	"""
	try:
		# import pdb; pdb.set_trace()
		if not isinstance(data, str): 
	  		df = pd.read_excel(data)
		else:
			Ops_mng = OperationManager()
			df_data = Ops_mng.execute_operation("database", "fetch_using_query",
		                                 (data))
			df = pd.DataFrame(df_data, columns=df_data[0].keys())

	except Exception as ex:
	  print("Error while processing the data {}".format(str(ex)))
	  df = None
	return df


def clear_data(path):
	"""
	Method to remove file/directory
	"""
	try:
	  shutil.rmtree(path)
	except:
		pass
        
