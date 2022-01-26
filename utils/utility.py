import pandas as pd
import os

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
	try:
	  if os.exists(path):
	  	os.system(path)
	  	os.system('Y')
	except:
		pass
        
