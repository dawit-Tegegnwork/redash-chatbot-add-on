from flask import Blueprint, jsonify, current_app as app

data_controller = Blueprint('data_controller', __name__)

import sys
import os

# Get the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_dir = os.path.dirname(current_dir)

# Get the grandparent directory
grandparent_dir = os.path.dirname(parent_dir)

# Add the grandparent directory to the system path
sys.path.insert(0, grandparent_dir)


from backend.models import cities, content_type, device_type, geography, new_and_returning_viewers
from backend.utils.db_utils import DatabaseManager
from backend.utils.helpers import extract_data_from_csv


# Connection profile
database_name = "postgres"
vehicle_table_name = "vehicle"
vehicle_path_table_name = "vehicle_path"
csv_file_path = "extract/data-files/traffic-data.csv"


# Define the connection string
connection_string = 'postgresql+psycopg2://postgres:postgres@localhost:5432/postgres'

# Create an instance of DatabaseManager
db_manager = DatabaseManager(connection_string)

def create_database():
    try:
        db_manager.create_database()
    except Exception as e:
        print(f"An error occurred while creating the database: {e}")

async def create_tables():
    try:
        db_manager.create_tables()
        return True
    except Exception as e:
        print(f"An error occurred while creating the tables: {e}")
        return False

async def load_data_into_database():
    try:
        cities_chart_data = extract_data_from_csv('data/cities/Chart data.csv')
        cities_table_data = extract_data_from_csv('data/cities/Table data.csv')
        citities_total = extract_data_from_csv('data/cities/Totals.csv')
        db_manager.insert_data(cities.CitiesChartData, cities_chart_data)
        db_manager.insert_data(cities.CitiesTableData, cities_table_data)
        db_manager.insert_data(cities.CitiesTotals, citities_total)

        return True
     
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

@data_controller.route('/load-data', methods=['GET'])
async def load_data():
    if await create_tables() and await load_data_into_database():
        return "Data loaded successfully", 200
    else:
        return "Failed to load data", 500