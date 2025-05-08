from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# extensions
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'admin.login'

# application factory
def create_app(config_class=None):
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app