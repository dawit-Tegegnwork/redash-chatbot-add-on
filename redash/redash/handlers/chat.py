from flask import request, jsonify
from redash.handlers.base import (
    BaseResource
)
import os
import requests
from openai import OpenAI
VARIABLE_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(
  api_key=VARIABLE_KEY
)

endpoint = 'http://192.168.8.114:5000/chat'

class ChatResource(BaseResource):
    def post(self):
        try:
            value = request.get_json()
            question = value.get('question')
            print(question)
            data = {"question": question}
            answer = requests.post(endpoint, json=data)
            print(answer)
            response_data = {"answer": answer}
            return jsonify(response_data), 200
        except Exception as error:
            print(error)
            return jsonify({"error": "An error occurred"}), 500