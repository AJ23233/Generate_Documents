# Filename: document_ops.py
# Description: This file contains all the operations that needs to be perform on/using the database
# Author: Ajay Vanara


from sqlalchemy import create_engine, text
from utils.db_connection import DatabaseConnection

class DatabaseOps:
	"""
	This class contains all the opetrations needs to be performed on/using database
	"""

	def __init__(self):
		pass

	def fetch_using_query(self, query):
		# Method to fetch data using query
		try:
			with DatabaseConnection() as db_obj:
				res = db_obj.execute(text(str(query))).all()
				return res
		except Exception as ex:
			print("Error while fetching data using query is :{}".format(str(ex)))
			return None
