# Filename: utility.py
# Description: This file contains all the operations that needs to be perform on the documents
# Author: Ajay Vanara

import pandas as pd
import os
import shutil

def data_proccessing(path):
	"""
	This method is used to fetched data
	"""
	try:
	  data = pd.read_excel(path)
	except Exception as ex:
	  print("Error while processing the data {}".format(str(ex)))
	  data = None
	return data


def clear_data(path):
	"""
	Method to remove file/directory
	"""
	try:
	  shutil.rmtree(path)
	except:
		pass
        
