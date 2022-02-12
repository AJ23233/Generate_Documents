# Filename: entity.py
# Description: This file contains all database table required for fetching data
# Author: Ajay Vanara

from db_connection import SQLAlchemyDB
from models.entity import EmployeeData

class QueryManager:
	def __init__(self):

		pass

	def fetch_employee_data():
		"""
		Method to fetch data from empoyee_data table 
		"""
		try:
			with SQLAlchemyDB() as db_obj:
				res = db_obj.session.query(EmployeeData.employee_id,
										   EmployeeData.name,
										   EmployeeData.age,
										   EmployeeData.svc_len,
										   EmployeeData.city_name,
										   EmployeeData.depart_name,
										   EmployeeData.job_title
											).all()
		except Exception as ex:
			print("Error while fetching the employee data is :{}".format(str(ex)))
			res = None
		return res