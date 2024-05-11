from backend.services.redash_api_client import RedashAPIClient
# from langchain.agents import tool
from typing import Optional
from typing import List, Tuple

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the Redash API key and Redash URL from the environment
api_key = os.getenv("REDASH_API_KEY")
api_url = os.getenv("REDASH_API")
data_source = os.getenv("REDASH_DATA_SOURCE")

Redash = RedashAPIClient(api_key, api_url)

# @tool
def create_redash_query(query: str, name: str, data_source_id: int = data_source, description: str="", options: dict=None):
    """Create a query in Redash and return the response json"""
    response = Redash.create_query(data_source_id, name, query, description, options)
    if response.status_code == 200:
        # Extract ID from response JSON
        query_id = response.json()['id']
        return query_id
    else:
        # Print error message and return None
        print(f"Failed to create query. Status code: {response.status_code}")
        return None

# @tool
def create_redash_visualization(query_id: int, visualization_type: str, name: str,columns:list=None,  x_axis:str=None, y_axis: list=None):
    """Create a visualization in Redash and return the response json"""
    response = Redash.create_visualization(qry_id=query_id, _type=visualization_type, name=name,columns=columns, x_axis=x_axis, y_axis=y_axis)
    if response.status_code == 200:
        # Extract ID from response JSON
        visualization_id = response.json()['id']
        return visualization_id
    else:
        # Print error message and return None
        print(f"Failed to create visualization. Status code: {response.status_code}")
        return None

# @tool
def create_redash_dashboard(name: str):
    """Create a dashboard in redash and return the response json"""
    response = Redash.create_dashboard(name)
    if response.status_code == 200:
        # Extract ID from response JSON
        dashboard_id = response.json()['id']
        return dashboard_id
    else:
        # Print error message and return None
        print(f"Failed to create dashboard. Status code: {response.status_code}")
        return None

# @tool
def add_widget_on_dashboard(dashboard_id: int, text: str="", visualization_id: int=None, full_width: bool=False, position: dict=None):
    """Add a widget in redash dashboard and return the response json"""
    response = Redash.add_widget(dashboard_id, text, visualization_id, full_width, position)
    if response.status_code == 200:
        # Extract ID from response JSON
        widget_id = response.json()['id']
        return widget_id
    else:
        # Print error message and return None
        print(f"Failed to create widget. Status code: {response.status_code}")
        return None

# @tool
def publish_dashboard(self, dashboard_id: int):
    """ Publish dashboard and return the response json"""
    response = Redash.publish_dashboard(dashboard_id)
    if response.status_code == 200:
        # Extract ID from response JSON
        dashboard_id = response.json()['id']
        return dashboard_id
    else:
        # Print error message and return None
        print(f"Failed to create dashboard. Status code: {response.status_code}")
        return None

# response = create_redash_visualization(query_id=34, visualization_type= "line", name= "Second Visualization", x_axis="Date", y_axis=[
#     {"type": "line", "name": "Views", "label": "c2"}
# ])