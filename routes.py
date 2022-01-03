# -*- coding: utf-8 -*-

import connexion
from flask import request, jsonify
from Operations.generate_doc import Genreate_doc


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


@APP.route("/v1/create_document", methods=['GET'])
def create_Documents():
    """
    This routes is used for creating the documents
    """
    response = Doc_obj.processs_data()
    return response

@APP.route("/v1/fetch_document/<id>", methods=['GET'])
def fetch_document(id):
    
    response = Doc_obj.read_docx(id)
    return response