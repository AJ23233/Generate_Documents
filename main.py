# -*- coding: utf-8 -*-

# !/usr/bin/.cs_env python3

from routes import APP

APP.add_api("swagger.yml")

if __name__ == "__main__":
    APP.run(host = '0.0.0.0',debug=True)