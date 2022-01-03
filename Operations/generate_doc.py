from docxtpl import DocxTemplate
import pandas as pd
import os
from flask import send_file

class Genreate_doc:
  """
  This class Contains the operations to generate the documents 
  """
  def __init__(self):
    pass

  def data_procesing(self,path):
    """
    This method is used to fetched and procesed data as per the requirements
    """
    try:
      data = pd.read_excel(path)
      data = data.drop(['termreason_desc','termtype_desc'], axis=1)
      new_cols = {'length_of_service':'svc_len', 'department_name':'Depart_name'}
      data.rename(columns = new_cols, inplace = True)
    except Exception as ex:
      print("Error while processing the data {}".format(str(ex)))
      data = None
    return data


  def generate_docs(self,row):
    """
    This method is used to generate the documents using the docxtpl object 
    """
    try:
      doc = DocxTemplate("./Doc_Templates/Docs/Appreciate_template.docx")
      context= row.to_dict()
      doc.render(context)
      path= "./Output/{}.docx".format(str(row['EmployeeID']))
      doc.save(path)
      print("{}.docx  saved successfully".format(str(row['EmployeeID'])))
    except Exception as ex:
      print("Error while generating the document {}".format(str(ex)))

  def processs_data(self):
    try:
      file_path = "./Doc_Templates/employee_details.xlsx"
      data = self.data_procesing(file_path)
      data.apply(self.generate_docs, axis=1)
      return "Documents Created successfully"
    except Exception as ex:
      return "Error while processing data {}".format(str(ex))

  def read_docx(self,id):
    try:
      file_name = str(id)+".docx"
      for i,j,k in os.walk("./Output/"):
        if file_name in k:
          path = os.path.join( os.path.join(os.path.realpath("Output"),file_name))
          print(path)
          return send_file(path, attachment_filename=file_name)
    except Exception as ex:
      print("Error while fetching doc : {}".format(str(ex)))
      return "error while fetching the document"