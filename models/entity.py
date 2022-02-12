# Filename: entity.py
# Description: This file contains all database table required for fetching data
# Author: Ajay Vanara

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
Metadata = Base.metadata

class EmployeeData(Base):
	"""
	This is the schema of employee_data tablle present in public schema
	"""

	__tablename__ = 'employee_data'
	__table_args__ = {'schema' : 'public'}

	employee_id = Column(Integer, primary_key=True)  
	name = Column(String(80))         
	age = Column(Integer)          
	svc_len = Column(Integer)      
	city_name = Column(String(80))    
	depart_name = Column(String(80))  
	job_title = Column(String(80))    
	gender = Column(String(80))       
	status_year = Column(String(80))  
	status = Column(String(80))       
	business_unit = Column(String(80))