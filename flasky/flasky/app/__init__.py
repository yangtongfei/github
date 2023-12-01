from flask import Flask, render_template, session
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user, login_required
import config


moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app():
	app = Flask(__name__)
	app.config.from_object(config)
	
	moment.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)

	from .main import main 
	app.register_blueprint(main)
	
	from .auth import auth
	app.register_blueprint(auth, url_prefix='/auth')


	return app
