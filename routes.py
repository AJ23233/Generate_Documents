# -*- coding: utf-8 -*-
# Filename: routes.py
# Description: This file contains all the application routes
# Author: Ajay Vanara

import connexion
from flask import request, jsonify, send_from_directory, send_file, render_template
from io import BytesIO

from Operations.Operation_manager import OperationManager
from config import CONF

APP = connexion.App(__name__, specification_dir='./')

Ops_mng = OperationManager()


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


@APP.route("/", methods=['GET'])
def test():
    return render_template("./download.html")


@APP.route("/v1/download/template_guide", methods=['GET'])
def download_template():
    
    # response = Doc_obj.download_template()
    response = Ops_mng.execute_operation("document", "download_template")
    if response:
        return response
    return "Error while downloading the template"


@APP.route("/v1/create_documents", methods=['POST'])
def create_doc():
    try:
        template = request.files['Template']
        data = request.files['Data']
        res_format = request.form.get("format")
        response = Ops_mng.execute_operation("document", "Create_docs",
                                             (template, data, res_format))
        return response
    except Exception as ex:
        print("Error while creating documents is : {}".format(str(ex)))
        return "Error while creating documents"


@APP.route("/v1/query-documents", methods=['POST', 'GET'])
def query_doc():
    try:
        template = request.files['Template']
        data = request.args['Data']
        res_format = request.form.get("format")
        response = Ops_mng.execute_operation("document", "Create_docs",
                                             (template, data, res_format))

        if 'Error' in response:
            raise Exception(response)
        return response
    except Exception as ex:
        print("Error while creating query documents is : {}".format(str(ex)))
        return "Error while creating documents using query"