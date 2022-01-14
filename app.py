from flask import Flask, jsonify, request
import json
app = Flask(__name__)

developer_list = [{'id': 0,
                   'name': 'Elber',
                   'habilities': ['Python', 'Flask']},
                  {'id': 1,
                      'name': 'Rafael',
                   'habilities': ['Python', 'Django']}]


@app.route("/dev/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    if request.method == 'GET':
        try:
            response = developer_list[id]
        except IndexError:
            response = {"statuscode": 404,
                        "message": "Id does not exist"}
        except Exception as e:
            response = {"statuscode": 400,
                        "message": e}
        return jsonify(response)
    elif request.method == 'PUT':
        developer_list[id] = json.loads(request.data)
        return jsonify(developer_list[id])
    elif request.method == 'DELETE':
        developer_list.pop(id)
        return jsonify(developer_list)


@app.route("/dev/", methods=['GET', 'POST'])
def developers():
    if request.method == 'GET':
        response = developer_list
        return jsonify(response)
    elif request.method == 'POST':
        dev = json.loads(request.data)
        last_id = developer_list[-1]['id']
        dev.update({'id': last_id + 1})
        developer_list.append(dev)
        return jsonify(developer_list[-1])
