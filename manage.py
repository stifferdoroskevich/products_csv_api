from flask_script import Manager
from rest_api import ingest
from rest_api import app

manager = Manager(app)

@manager.command
def init_db():
    ingest.init_db()

@manager.command
def drop_db():
    ingest.drop_db()


if __name__ == "__main__":
    manager.run()