from flask import Blueprint, jsonify

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
    print('we go here')
    return jsonify({"dashboards": list(redash_dashboards.values())})

@dashboard_controller.route('/redash/dashboard/<dashboard_id>', methods=['GET'])
def get_redash_dashboard(dashboard_id):
    dashboard = redash_dashboards.get(dashboard_id)
    if dashboard:
        return jsonify(dashboard)
    else:
        return jsonify({"status": "error", "message": "Dashboard not found"}), 404
