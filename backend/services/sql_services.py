# sql_services.py

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select

class SQLClient:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.metadata = MetaData(bind=self.engine)
        self.connection = self.engine.connect()

    def execute_query(self, query):
        """
        Execute a SQL query against the connected database and retrieve the results.
        """
        result = self.connection.execute(query)
        return result.fetchall()

    def get_table_schema(self, table_name):
        """
        Retrieve the schema of a table from the connected database.
        """
        return Table(table_name, self.metadata, autoload=True)

    def insert_data(self, table_name, data):
        """
        Insert data into a table in the connected database.
        """
        table = Table(table_name, self.metadata, autoload=True)
        self.connection.execute(table.insert(), data)

    def update_data(self, table_name, condition, data):
        """
        Update data in a table in the connected database based on a condition.
        """
        table = Table(table_name, self.metadata, autoload=True)
        update_stmt = table.update().where(condition).values(data)
        self.connection.execute(update_stmt)

    def delete_data(self, table_name, condition):
        """
        Delete data from a table in the connected database based on a condition.
        """
        table = Table(table_name, self.metadata, autoload=True)
        delete_stmt = table.delete().where(condition)
        self.connection.execute(delete_stmt)

    def query_table(self, table_name, columns=None):
        """
        Query all rows from a table in the connected database.
        """
        table = Table(table_name, self.metadata, autoload=True)
        if columns:
            query = select(columns).select_from(table)
        else:
            query = select([table])
        result = self.connection.execute(query)
        return result.fetchall()
