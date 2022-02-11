# Filename: document_ops.py
# Description: This file contains all the operations that needs to be perform on the documents
# Author: Ajay Vanara

import io
import os
from flask import send_file
from docxtpl import DocxTemplate
import pandas as pd
from docx2pdf import convert  
import zipfile
from sys import platform

# imports from other directories 
from utils.utility import generate_df, clear_data
from config import CONF

class DocumentOps:
  """
  This class Contains the operations to generate the documents 
  """
  def __init__(self):
    self.template_doc = os.path.join(os.path.dirname
                        (os.path.dirname(os.path.abspath(__file__))),
                        CONF['directory']['templates'])
    self.docs = os.path.join(os.path.dirname(
                self.template_doc), CONF['directory']['doc'])
    self.pdfs = os.path.join(os.path.dirname(
                self.template_doc), CONF['directory']['pdf'])

  # def data_procesing(self,path):
  #   """
  #   This method is used to fetch data 
  #   """
  #   try:
      
  #     data = pd.read_excel(path)

  #   except Exception as ex:
  #     print("Error while processing the data {}".format(str(ex)))
  #     data = None
  #   return data


  def generate_docs(self, row, docx, doc_name=None):
    """
    This method generates the documents using the docxtpl object 
    """
    try:
      doc = DocxTemplate(docx)
      context= row.to_dict()
      doc.render(context)
      name = doc_name or row.index[0]
      path = os.path.join(self.docs, str(row[name])+'.docx')
      doc.save(path)
      print("{}.docx  saved successfully".format(str(row[name])))
    except Exception as ex:
      print("Error while generating the document {}".format(str(ex)))


  def Create_docs(self, docx, data, format):
    """
    This Method is used to create documents
    """
    try:
      # creates word dcuments from dataframe
      data_df = generate_df(data)
      if not os.path.exists(self.docs):
        os.mkdir(self.docs)

      data_df.apply(self.generate_docs, docx=docx, axis=1)

      res_files = self.docs
      # creates pdfs from word docs 
      if format == 'pdf':
        res_files  = self.generate_pdfs()

      zipped_file = self.zipdir(res_files)
      if zipped_file:
        print("zipped documents successfully")
        return  send_file(zipped_file, 
                         mimetype="application/zip",
                         attachment_filename=CONF['file_names']['zip'],
                         as_attachment=True)
      raise Exception("Zipped file not found")
    except Exception as ex:
      print("Error while creating doc : {}".format(str(ex)))
      return "Error while creating the document"


  # @staticmethod
  # def generate_df(data):
  #   try:
  #     if isinstance(data, object):
  #       res = data_proccessing(data)
  #     else:
  #       res = make_dataframe(data)
  #   except Exception as ex:
  #     print("Error while generating the dataframe :{}".format(str(ex)))
  #     res = None
  #   return res



  def generate_pdfs(self):
    """
    Method to create .pdf documents from .docx
    """
    try:
      if not os.path.exists(self.pdfs):
        os.mkdir(self.pdfs)

      if platform == 'linux':
        os.system(f"libreoffice --headless --convert-to pdf {self.docs}/*.docx --outdir {os.path.relpath(self.pdfs)}")
      else:
        os.system(f"docx2pdf {self.docs} {self.pdfs}")

      print("PDF Documents Created successfully")
      return self.pdfs
    except Exception as ex:
      print("Error while creating pdf is :{}".format(str(ex)))
      return self.docs


  def zipdir(self, path):
    """
    Method to zip the documents 
    """
    try:
      with zipfile.ZipFile(CONF['file_names']['zip'], mode='w') as ziph:
        for root, dirs, files in os.walk(path):
          for file in files:
              ziph.write(os.path.relpath(os.path.join(root, file)))
    except Exception as ex:
      print("Error while zipping the files : {}".format(str(ex)))
      res = None
    return os.path.join(os.path.dirname(self.pdfs), CONF['file_names']['zip'])


  def download_template(self):
    """
    Method to download the template document
    """
    try:
      file_name = CONF['file_names']['template_guide']
      file_path = os.path.join(self.template_doc, 'Docs', file_name)
      return send_file(file_path, attachment_filename=file_name, as_attachment=True)
    except Exception as ex:
      print("Error while fetching doc : {}".format(str(ex)))
      return None


  def remove_docs(self):
    """
    Method to remove documents
    """
    clear_data(self.docs)
    clear_data(self.pdfs)
    clear_data(os.path.join(os.path.dirname(self.pdfs), CONF['file_names']['zip']))
    print("successfully removed docs")
