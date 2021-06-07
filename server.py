from rest_api import app, config

if __name__ == '__main__':
    app.config.from_object('rest_api.config')
    app.run()
