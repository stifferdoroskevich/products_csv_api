from flask_script import Manager
from CRUD import db_csv
from app import app

manager = Manager(app)

@manager.command
def init_db():
    db_csv.create_db()

@manager.command
def drop_db():
    db_csv.drop_db()


if __name__ == "__main__":
    manager.run()