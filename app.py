from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import signs
from werkzeug import exceptions


app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200

if __name__ == "__main__":
    app.run(debug=True)