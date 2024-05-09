from flask import Blueprint, jsonify, current_app as app

chat_controller = Blueprint('chat_controller', __name__)

# Sample data for chat messages
chat_messages = [{"hello": "holla"}]

@chat_controller.route('/chat', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message')
    if message:
        chat_messages.append(message)
        return jsonify({"status": "success", "message": "Message sent successfully"})
    else:
        return jsonify({"status": "error", "message": "Message cannot be empty"}), 400

@chat_controller.route('/chat', methods=['GET'])
def get_messages():
    with app.app_context():
        return jsonify({"messages": chat_messages})
