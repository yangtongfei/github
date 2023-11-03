from flask import Flask, render_template
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import config


moment = Moment()
db = SQLAlchemy()


def create_app():
	app = Flask(__name__)
	app.config.from_object(config)
	
	moment.init_app(app)
	db.init_app(app)

	from .main import main 
	app.register_blueprint(main)
	
	
	from .auth import auth
	app.register_blueprint(auth, url_prefix='/auth')


	return app
