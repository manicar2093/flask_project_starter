from flask import Flask
from app.dbs import db, mongo
from app.migrate import migrate
from app.web.routes import site

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    mongo.init_app(app)
    migrate.init_app(app)

    app.register_blueprint(site)

    return app