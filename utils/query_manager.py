# Filename: entity.py
# Description: This file contains all database table required for fetching data
# Author: Ajay Vanara

from utils.db_connection import SQLAlchemyDB
from models.entity import EmployeeData

class QueryManager:
	"""
	This class is used to fetch records from database using Sqlalchemy-ORM 
	"""

	def __init__(self):

		pass

	def fetch_employee_data(self):
		"""
		Method to fetch data from empoyee_data table 
		"""
		try:
			# import pdb; pdb.set_trace()
			with SQLAlchemyDB() as db_obj:
				res = db_obj.query(EmployeeData.employee_id,
								EmployeeData.name.label('Name'),
								EmployeeData.age.label('Age'),
								EmployeeData.svc_len,
								EmployeeData.city_name,
								EmployeeData.depart_name.label('Depart_name'),
								EmployeeData.job_title,
								EmployeeData.gender,
								EmployeeData.business_unit.label('BUSINESS_UNIT')
									).all()
				print(res)
		except Exception as ex:
			print("Error while fetching the employee data is :{}".format(str(ex)))
			res = None
		return res