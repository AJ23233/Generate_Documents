# -*- coding: utf-8 -*-

import connexion
from flask import request, jsonify, send_from_directory, send_file, render_template
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


@APP.route("/v1/create_documents", methods=['POST', 'GET'])
def create_doc():
    try:
        Template = request.files['Template']
        Data = request.files['Data']
        response = Doc_obj.Create_docs(Template, Data)
        if 'Error' in response:
            raise Exception(response)
        return send_file(response, mimetype='application/zip', attachment_filename="files.zip", as_attachment=True)
    except Exception as ex:
        print("Error while creating documents is : {}".format(str(ex)))
        return "Error while creating documents"
    # finally:
    #     Doc_obj.remove_docs()

        

@APP.route("/", methods=['GET'])
def test():
    return render_template("./download.html")


@APP.route("/v1/download/template_guide", methods=['GET'])
def download_template():
    
    response = Doc_obj.download_template()
    if response:
        return response
    return "Error while downloading the template"