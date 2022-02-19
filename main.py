# -*- coding: utf-8 -*-

# !/usr/bin/.cs_env python3

from routes import APP

APP.add_api("swagger.yml")

app = APP

if __name__ == "__main__":
    # APP.run()
    app.run()