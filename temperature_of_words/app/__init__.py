from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prod_db.sqlte3'

    db.init_app(app)
    migrate.init_app(app, db)

    from app import main_route, search_route, login_route
    app.register_blueprint(main_route.bp)
    app.register_blueprint(search_route.bp, url_prefix='/search')
    app.register_blueprint(login_route.bp, url_prefix='/login')

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)