from flask import Flask

app = Flask(__name__)

from app import routes # import here to avoid circular dependencies