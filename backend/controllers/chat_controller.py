from flask import Blueprint, jsonify, request, current_app as app
import os
from openai import OpenAI
import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
  api_key=api_key
)


chat_controller = Blueprint('chat_controller', __name__)

# Sample data for chat messages
chat_messages = [{"hello": "holla"}]

@chat_controller.route('/chat', methods=['POST'])
def send_message():
        try:
            value = request.get_json()
            question = value.get('question')
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a redash visualization assistant, skilled in SQL queries and data visualization. You are only required to give answers for query and data visualization questions. If asked about a topic outside these two, make sure to respond that you have no information regarding that question. I am only here to help you with your query and data visualization questions. When asked to write queries, only provide the code without descriptions."},
                    {"role": "user", "content": question}
                ]
            )
            answer = completion.choices[0].message.content
            response_data = {"answer": answer}
            return jsonify(response_data), 200
        except Exception as error:
            print(error)
            return jsonify({"error": "An error occurred"}), 500


@chat_controller.route('/chat', methods=['GET'])
def get_messages():
    with app.app_context():
        return jsonify({"messages": chat_messages})
