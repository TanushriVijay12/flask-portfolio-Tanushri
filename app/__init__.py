from flask import Flask

def create_app(config_class=None):
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Import and register blueprint
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
