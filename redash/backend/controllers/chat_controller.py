from flask import Blueprint, jsonify, current_app as app
from quart import request
chat_controller = Blueprint('chat_controller', __name__)

import sys
import os

# Get the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_dir = os.path.dirname(current_dir)

# Get the grandparent directory
grandparent_dir = os.path.dirname(parent_dir)

# Add the grandparent directory to the system path
sys.path.insert(0, parent_dir)

from services.db_services import DatabaseManager
from services.nlp_services import generate_sql_query
from utils.helpers import read_schema_file
from services.redash_services import create_redash_query, create_redash_dashboard, create_redash_visualization

connection_string = 'postgresql+psycopg2://postgres:postgres@postgres:5432/postgres'

@chat_controller.route('/api/chat', methods=['POST'])
async def chat():
    try:
        # Get the question from the request body
        data = await request.get_json()
        question = data.get('question')

        if not question:
            return "Question not provided", 400

        db_manager = DatabaseManager(connection_string)  # Instantiate DatabaseManager
        schema = db_manager.read_database_schema()
        print('schema', schema)
        answer = generate_sql_query(question, schema)   
        print("answer: ", answer)
        query_id = create_redash_query(answer, question)
        # if query_id:
        #     create_redash_visualization(query_id, "table", query_id )
        return answer, 200
    except Exception as e:
        return str(e),  500