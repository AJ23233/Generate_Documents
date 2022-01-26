# Author: Ajay Vanara


import io
import os
from flask import send_file
from docxtpl import DocxTemplate
import pandas as pd
from docx2pdf import convert  
import zipfile

# imports from other directories 
from utils.utility import data_proccessing, clear_data

class Genreate_doc:
  """
  This class Contains the operations to generate the documents 
  """
  def __init__(self):
    self.template_doc = os.path.join(os.path.dirname(os.path.dirname
                        (os.path.abspath(__file__))),"Doc_Templates")
    self.Output = os.path.join(os.path.dirname(self.template_doc), 'Output')
    self.pdfs = os.path.join(os.path.dirname(self.template_doc), "pdf")


  def data_procesing(self,path):
    """
    This method is used to fetched data as per the requirements
    """
    try:
      data = pd.read_excel(path)
    except Exception as ex:
      print("Error while processing the data {}".format(str(ex)))
      data = None
    return data


  def generate_docs(self, row, docx, doc_name=None):
    """
    This method generates the documents using the docxtpl object 
    """
    try:
      doc = DocxTemplate(docx)
      context= row.to_dict()
      doc.render(context)
      name = doc_name or row.index[0]
      path = os.path.join(self.Output, str(row[name])+'.docx')
      doc.save(path)
      print("{}.docx  saved successfully".format(str(row[name])))
    except Exception as ex:
      print("Error while generating the document {}".format(str(ex)))


  def Create_docs(self, docx, data):
    """
    This Method is used to create documents
    """
    try:
      # creates word dcuments from dataframe
      data_df = data_proccessing(data)
      if not os.path.exists(self.Output):
        os.mkdir(self.Output)

      data_df.apply(self.generate_docs, docx=docx, axis=1)

      # creates pdfs from word docs 
      pdf_files  = self.generate_pdfs()

      zipped_file = Genreate_doc.zipdir(pdf_files)
      if zipped_file:
        print("zipped documents successfully")
        return zipped_file
      return "Error while creating documents"
    except Exception as ex:
      print("Error while creating doc : {}".format(str(ex)))
      return "Error while creating the document"


  def generate_pdfs(self):
    """
    Method to create .pdf documents from .docx
    """
    try:
      if not os.path.exists(self.pdfs):
        os.mkdir(self.pdfs)
      os.system(f"docx2pdf {self.Output} {self.pdfs}")

      print("PDF Documents Created successfully")
      return self.pdfs
    except Exception as ex:
      print("Error while creating pdf is :{}".format(str(ex)))
      return self.Output


  @staticmethod
  def zipdir(path):
    """
    Method to zip the documents 
    """
    try:
      import pdb; pdb.set_trace()
      res = io.BytesIO()
      with zipfile.ZipFile(res, mode='w') as ziph:
        for root, dirs, files in os.walk(path):
          for file in files:
              ziph.write(os.path.join(root, file), os.path.basename(file))
      res.seek(0)
    except Exception as ex:
      print("Error while zipping the files : {}".format(str(ex)))
      res = None
    return res


  def download_template(self):
    """
    Method to download the template document
    """
    try:
      file_name = 'Template_Guide.docx'
      file_path = os.path.join(self.template_doc, 'Docs', file_name)
      return send_file(file_path, attachment_filename=file_name, as_attachment=True)
    except Exception as ex:
      print("Error while fetching doc : {}".format(str(ex)))
      return None


  def remove_docs(self):
    clear_data(self.Output)
    clear_data(self.pdfs)
    print("successfully removed docs")