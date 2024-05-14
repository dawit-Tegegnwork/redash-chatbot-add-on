from flask import Blueprint, jsonify, current_app

dashboard_controller = Blueprint('dashboard_controller', __name__)

# Sample data for Redash dashboards
redash_dashboards = {
    "sales_dashboard": {
        "id": 1,
        "name": "Sales Dashboard",
        "url": "http://redash.example.com/dashboard/1",
        "description": "Dashboard for sales analytics"
    },
    "customer_dashboard": {
        "id": 2,
        "name": "Customer Dashboard",
        "url": "http://redash.example.com/dashboard/2",
        "description": "Dashboard for customer analytics"
    }
}

@dashboard_controller.route('/redash/dashboards', methods=['GET'])
def get_redash_dashboards():
    with current_app.app_context():
        dashboards = list(redash_dashboards.values())
        return jsonify({"dashboards": dashboards, "status": "success", "message": "Dashboards retrieved successfully"})

@dashboard_controller.route('/redash/dashboard/<dashboard_id>', methods=['GET'])
def get_redash_dashboard(dashboard_id):
    with current_app.app_context():
        dashboard = redash_dashboards.get(dashboard_id)
        if dashboard:
            return jsonify({"dashboard": dashboard, "status": "success", "message": "Dashboard retrieved successfully"})
        else:
            return jsonify({"status": "error", "message": "Dashboard not found"}), 404
