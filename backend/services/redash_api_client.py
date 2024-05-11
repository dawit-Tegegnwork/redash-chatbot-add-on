import requests

class RedashAPIClient:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url

    def create_query(self, data_source_id, name, query, description="", options=None):
        endpoint = f"{self.api_url}/queries"
        headers = {
            "Authorization": f"Key {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "data_source_id": data_source_id,
            "name": name,
            "query": query,
            "description": description,
            "options": options or {}
        }
        return requests.post(endpoint, headers=headers, json=payload)

    def create_visualization(self, qry_id, _type, name, columns=None, x_axis=None, y_axis=None):
        endpoint = f"{self.api_url}/visualizations"
        headers = {
            "Authorization": f"Key {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "query_id": qry_id,
            "type": _type,
            "name": name,
            "columns": columns or [],
            "x_axis": x_axis,
            "y_axis": y_axis or []
        }
        return requests.post(endpoint, headers=headers, json=payload)

    def create_dashboard(self, name):
        endpoint = f"{self.api_url}/dashboards"
        headers = {
            "Authorization": f"Key {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "name": name
        }
        return requests.post(endpoint, headers=headers, json=payload)

    def add_widget(self, dashboard_id, text="", visualization_id=None, full_width=False, position=None):
        endpoint = f"{self.api_url}/widgets"
        headers = {
            "Authorization": f"Key {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "dashboard_id": dashboard_id,
            "type": "visualization",
            "text": text,
            "visualization_id": visualization_id,
            "options": {
                "position": position or {},
                "visualization": {
                    "width": "auto" if full_width else 1
                }
            }
        }
        return requests.post(endpoint, headers=headers, json=payload)

    def publish_dashboard(self, dashboard_id):
        endpoint = f"{self.api_url}/dashboards/{dashboard_id}/public"
        headers = {
            "Authorization": f"Key {self.api_key}"
        }
        return requests.post(endpoint, headers=headers)
