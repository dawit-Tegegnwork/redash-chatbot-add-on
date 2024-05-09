from quart import Quart
from config import Config
from models import cities, content_type
from controllers.chat_controller import chat_controller
from controllers.dashboard_controller import dashboard_controller

def create_app():
    app = Quart(__name__)
    app.config.from_object(Config)

    # Initialize database
    # db.init_app(app)

    # Register blueprints
    app.register_blueprint(chat_controller)
    app.register_blueprint(dashboard_controller)

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
