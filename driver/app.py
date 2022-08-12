#!/usr/bin/env python3

from posixpath import split
from pprint import pprint
import json

from flask import Flask, render_template, request, redirect, jsonify

from model import Model
from helper import shaping

app = Flask(__name__)


@app.route('/')
def index():
    model = Model()
    nodes = model.get_nodes()
    model.close()
    return render_template('index.html', nodes=nodes)


@app.route('/api/nodes')
def get_nodes():
    model = Model()
    nodes = model.get_nodes_summary()
    model.close()

    return jsonify(nodes)


@app.route('/api/node/<node_id>', methods=['GET'])
def get_node(node_id):
    model = Model()
    node = model.get_node_summary(node_id)[0]
    model.close()

    return jsonify(node)


@app.route('/api/node/<node_id>', methods=['POST'])
def post_node(node_id):
    data = request.data.decode('utf-8')
    data = json.loads(data)
    auto_control = data["auto_control"]
    preset_temp = data["preset_temp"]

    model = Model()
    model.set_node_auto_control_and_preset_temp(
        node_id, auto_control, preset_temp)
    node = model.get_node_summary(node_id)[0]

    model.commit()
    model.close()

    return jsonify(node)


@app.route('/set-node', methods=['POST'])
def set_node():
    model = Model()
    form_dict = {}

    for k, v in request.form.items():
        prop_name, idx = k.split("-")

        if idx not in form_dict:
            form_dict[idx] = {}

        if v.lower() == "none" or v.lower() == "null":
            v = None

        form_dict[idx][prop_name] = v

    for idx, row in form_dict.items():
        sensor_mac = row["sensor_mac"]
        plug_mac = row["plug_mac"]
        preset_temp = row["preset_temp"]
        location_name = row["location_name"]

        model.set_node(idx, sensor_mac, plug_mac, preset_temp, location_name)

    model.commit()
    model.close()

    return redirect("/")


@app.route('/set-preset-temp', methods=['POST'])
def set_preset_temp():
    model = Model()
    for k, v in request.form.items():
        prop_name, idx = k.split("-")
        if prop_name != "preset_temp":
            continue

        model.set_preset_temp(idx, v)

    model.commit()
    model.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8888)
