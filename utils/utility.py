# Filename: utility.py
# Description: This file contains all the operations that needs to be perform on the documents
# Author: Ajay Vanara

import pandas as pd
import os
import shutil
from Operations.Operation_manager import OperationManager
from importlib import import_module 

def generate_df(data):
	"""
	This method is used to generate dataframe
	data should be in excel or in query format 
	"""
	try:
		if isinstance(data, str):
			Ops_mng = OperationManager()
			df_data = Ops_mng.execute_operation("database", "fetch_using_query",
		                                 (data))
			df = pd.DataFrame(df_data, columns=df_data[0].keys())
		elif isinstance(data, dict):
			df = create_df(data)
		else:
			df = pd.read_excel(data)
	except Exception as ex:
	  print("Error while generating the dataframe {}".format(str(ex)))
	  df = None
	print(df)
	return df

def create_df(data):
	"""
	This method is used when data needs to fetch using existing orm queries
	"""
	try:
		cls = getattr(import_module("utils.query_manager"),"QueryManager")
		method = getattr(cls(), data['method'])
		if data.get('params', False) :
			df_data = method(params)
		else:
			df_data = method()
		df = pd.DataFrame(df_data, columns=df_data[0].keys())
		print(df)
	except Exception as ex:
		print("Error while creating ORM df {}".format(str(ex)))
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
        
