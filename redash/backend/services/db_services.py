from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from backend.models.base import Base

class DatabaseManager:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)

    def create_database(self, database_name):
        try:
            # Create database if not exists
            self.engine.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')
            print(f"Database '{database_name}' created successfully.")
        except Exception as e:
            print(f"Error creating database: {e}")

    def create_tables(self):
        try:
            # Create all tables if they don't exist
            Base.metadata.create_all(self.engine)
            print("Tables created successfully.")
        except Exception as e:
            print(f"Error creating tables: {e}")
    
    def read_database_schema(self):
        try:
            inspector = inspect(self.engine)
            tables = inspector.get_table_names()

            schema = {}
            for table_name in tables:
                columns = inspector.get_columns(table_name)
                schema[table_name] = [column['name'] for column in columns]

            print('The schema is ', schema)
            return schema
        except Exception as e:
            print(f"Error creating database: {e}")

    def insert_data(self, table_type, data):
        session = None
        try:
            session = self.Session()

            # Bulk insert data
            session.bulk_insert_mappings(table_type, data)

            session.commit()
            print("Data inserted successfully.")
        except Exception as e:
            if session:
                session.rollback()
            print(f"Error inserting data into database: {e}")
        finally:
            # Close session if it was opened
            if session:
                session.close()