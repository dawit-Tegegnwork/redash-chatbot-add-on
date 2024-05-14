from flask import Blueprint, jsonify, current_app as app

chat_controller = Blueprint('chat_controller', __name__)

import sys
import os

# Define the connection string
connection_string = 'postgresql+psycopg2://postgres:postgres@localhost:15432/postgres'


# Get the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_dir = os.path.dirname(current_dir)

# Get the grandparent directory
grandparent_dir = os.path.dirname(parent_dir)

# Add the grandparent directory to the system path
sys.path.insert(0, grandparent_dir)


from backend.services.db_services import DatabaseManager
from backend.services.nlp_services import generate_sql_query
from backend.utils.helpers import read_schema_file
from backend.services.redash_services import create_redash_query, create_redash_dashboard, create_redash_visualization

@chat_controller.route('/chat', methods=['POST'])
async def chat():
    if 1:
        schema_path = 'database/schema.sql'
        question = "which cities do we have out top customers"
        print(schema_path)
        # Create an instance of DatabaseManager
        db_manager = DatabaseManager(connection_string)
        schema = db_manager.read_database_schema()
        answer = generate_sql_query(question, schema)   
        print("answer: ", answer)
        query_id = create_redash_query(answer, "we did it")
        if(query_id):
            create_redash_visualization(query_id, )
        return "Data loaded successfully", 200
    else:
        return "Failed to load data", 500