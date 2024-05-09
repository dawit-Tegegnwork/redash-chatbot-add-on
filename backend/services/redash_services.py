import requests

class RedashClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key

    def create_dashboard(self, name, description=''):
        """
        Create a new dashboard in Redash.
        """
        endpoint = f"{self.base_url}/api/dashboards"
        headers = {'Authorization': f'Key {self.api_key}'}
        data = {'name': name, 'description': description}
        response = requests.post(endpoint, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def get_dashboards(self):
        """
        Retrieve information about existing dashboards in Redash.
        """
        endpoint = f"{self.base_url}/api/dashboards"
        headers = {'Authorization': f'Key {self.api_key}'}
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        return response.json()

    def configure_visualization(self, dashboard_id, visualization_id, visualization_config):
        """
        Configure a visualization within a dashboard in Redash.
        """
        endpoint = f"{self.base_url}/api/dashboards/{dashboard_id}/visualizations/{visualization_id}"
        headers = {'Authorization': f'Key {self.api_key}'}
        response = requests.put(endpoint, headers=headers, json=visualization_config)
        response.raise_for_status()
        return response.json()

    def execute_query(self, query_id, parameters=None):
        """
        Execute a query against the data sources connected to Redash and retrieve the results.
        """
        endpoint = f"{self.base_url}/api/queries/{query_id}/results"
        headers = {'Authorization': f'Key {self.api_key}'}
        response = requests.get(endpoint, headers=headers, params=parameters)
        response.raise_for_status()
        return response.json()
