from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask import Flask
import flask
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

manager = Manager(app)
db = SQLAlchemy(app)


if __name__ == '__main__':
    db.create_all()
    manager.run()