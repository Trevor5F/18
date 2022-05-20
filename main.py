from flask import Flask
from flask_restx import Api


from app.config import Config
from app.database import db
from app.views.books import book_ns
from app.views.authors import author_ns
from dao.model.author import Author
from dao.model.book import Book


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(book_ns)
    api.add_namespace(author_ns)


def load_data():
    b1 = Book(id=1, name='Harry Potter', year=2000,)
    b2 = Book(id=2, name='Le Comte de Monte-Cristo', year=1844)

    a1 = Author(id=1, first_name='Joan', last_name='Rowling')
    a2 = Author(id=2, first_name='Alexander', last_name='Dumas')


    db.create_all()

    with db.session.begin():
        db.session.add_all([b1, b2])
        db.session.add_all([a1, a2])


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)

    configure_app(app)
    load_data()

    app.run()
