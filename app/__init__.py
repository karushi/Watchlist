from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

boostrap = Bootstrap()
db = SQLAlchemy

# Initializing application
app = Flask(__name__, instance_relative_config=True)


# setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


# Initializing Flask Extensions
boostrap = Bootstrap(app)
# db.init_app(app)



from app import views
