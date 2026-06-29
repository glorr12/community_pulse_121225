import os
from pathlib import Path

from flask import Flask
from config import DevelopmentConfig, Config, TestConfig
from app.routers.questions import questions_bp
from app.routers.responses import responses_bp

from app.models import db, Migrate






print(os.environ.get('FLASK_DEBUG'))
print(os.environ.get('FLASK_ENV'))

def create_app():
    app = Flask(__name__)

    flask_mode = os.environ.get('FLASK_ENV', 'development')
    config_classes = {
        'development': DevelopmentConfig,
        'production': Config,
        'testing': TestConfig
    }.get(flask_mode)

    app.config.from_object(config_classes)

    db.init_app(app)

    migrate = Migrate()  # new
    migrate.init_app(app, db)

    app.register_blueprint(questions_bp, url_prefix='/questions')
    app.register_blueprint(responses_bp, url_prefix='/responses')

    return app