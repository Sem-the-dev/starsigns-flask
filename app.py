from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import signs
# from werkzeug import exceptions


app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200

@app.route('/api/signs', methods=['GET', 'POST'])
def signs_handler():
    fns = {
        'GET': signs.index,
        'POST': signs.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/api/signs/<int:sign_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def sign_handler(sign_id):
    fns = {
        'GET': signs.show,
        'PATCH': signs.update,
        'PUT': signs.update,
        'DELETE': signs.destroy
    }
    resp, code = fns[request.method](request, sign_id)
    return jsonify(resp), code

if __name__ == "__main__":
    app.run(debug=True)