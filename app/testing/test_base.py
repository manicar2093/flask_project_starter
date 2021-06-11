from app.app_factory import create_app
from app.dbs import db
from app.config import testing
import unittest
import flask_mongoengine

class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app(testing)
        cls.runner = cls.app.test_cli_runner()
        cls.client = cls.app.test_client()
        cls.db = db
        cls._mongo_con = flask_mongoengine.mongoengine.connection.get_connection()
        with cls.app.app_context():
            cls.db.create_all()
        
    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            # Elimina todas las tablas de la base de datos
            cls.drop_databases()

    @classmethod
    def drop_databases(cls):
        cls.drop_mongo_collection()
        cls.drop_sql_db()
            
    @classmethod
    def drop_mongo_collection(cls):
        cls._mongo_con.drop_database(cls.app.config['MONGODB_DB'])

    @classmethod
    def drop_sql_db(cls):
        cls.db.session.remove()
        cls.db.drop_all()
