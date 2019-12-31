import os

baseDir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "my-precious"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or f"sqlite:///{os.path.join(baseDir, 'microblog.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # to disable notifications if there are changes to the db

