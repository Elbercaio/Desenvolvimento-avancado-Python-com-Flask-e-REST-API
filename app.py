from flask import Flask, jsonify, request
import json
app = Flask(__name__)


@app.route("/<int:id>")
def users(id):
    return jsonify({'name': 'Elber',
                    'occupation': 'slave'})


@app.route("/sum", methods=["POST", "GET"])
def post_sum():
    if request.method == 'POST':
        data = json.loads(request.data)['values']
        return jsonify({'sum': sum(data)})
    if request.method == 'GET':
        return jsonify({'method': "GET"})


if __name__ == "__main__":
    app.run(debug=True)
