# Filename: config.py
# Description: This file contains all the operations that needs to be perform on the documents
# Author: Ajay Vanara

import configparser
from os import environ

CONF = configparser.ConfigParser()
CONF.read('config.properties')

DB_NAME = environ.get('DB_NAME') or CONF['database']['db_name']
DB_PORT = environ.get('DB_PORT') or CONF['database']['db_port']
DB_HOST = environ.get('DB_HOST') or CONF['database']['db_host']
DB_USER = environ.get('DB_USER') or CONF['database']['db_user']
DB_PASS = environ.get('DB_PASS') or CONF['database']['db_pass']
DB_TYPE= environ.get('DB_TYPE') or CONF['database']['db_type']

DB_URL = f"{DB_TYPE}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}" 

# export DB_NAME='doc_gen'
# export DB_PASS='python'
# export DB_USER='python'
# export DB_PORT=5432
# export DB_HOST='localhost'








