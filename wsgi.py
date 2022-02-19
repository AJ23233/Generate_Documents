from routes import APP

APP.add_api("swagger.yml")

if __name__ == "__main__":
    APP.run()