# -*- coding: utf-8 -*-
# Filename: routes.py
# Description: This file contains all the application routes
# Author: Ajay Vanara

import connexion
from flask import request, jsonify, send_from_directory, send_file, render_template
from io import BytesIO

from Operations.document_ops import Genreate_doc
from config import CONF

APP = connexion.App(__name__, specification_dir='./')

Doc_obj = Genreate_doc()


@APP.route("/v1/ping")
def ping():
    """
    ping-pong method
    Function to test the health of flask application
    Parameters: None
    Returns:
    string: "Pong"
    """
    return jsonify({"data":"Pong"})


@APP.route("/v1/create_documents", methods=['POST', 'GET'])
def create_doc():
    try:
        template = request.files['Template']
        data = request.files['Data']
        res_format = request.form.get("format")
        response = Doc_obj.Create_docs(template, data, res_format)
        
        if 'Error' in response:
            raise Exception(response)
        res = send_file(response, 
                         mimetype="application/zip",
                         attachment_filename=CONF['file_names']['zip'],
                         as_attachment=True)
        return res
    except Exception as ex:
        print("Error while creating documents is : {}".format(str(ex)))
        return "Error while creating documents"
    finally:
        Doc_obj.remove_docs()

        

@APP.route("/", methods=['GET'])
def test():
    return render_template("./download.html")


@APP.route("/v1/download/template_guide", methods=['GET'])
def download_template():
    
    response = Doc_obj.download_template()
    if response:
        return response
    return "Error while downloading the template"