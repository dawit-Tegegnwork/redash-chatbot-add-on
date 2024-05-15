from flask import request, jsonify
from redash.handlers.base import (
    BaseResource
)
from urllib import request as urlrequest
from urllib import error as urlerror
import json
# from flask_wtf.csrf import generate_csrf, csrf_exempt
import os
import requests

endpoint = 'http://localhost:5057/chat'

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
            return jsonify({"error": "An error occurred!"}), 500