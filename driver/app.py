#!/usr/bin/env python3

import datetime
from posixpath import split
from pprint import pprint

from flask import Flask, render_template, request, redirect

from model import Model

app = Flask(__name__)


@app.route('/')
def index():
    model = Model()
    nodes = model.get_nodes()
    model.close()
    return render_template('index.html', nodes=nodes)


@app.route('/view')
def view():
    model = Model()
    nodes = model.get_nodes_summary()
    model.close()
    now = datetime.datetime.now()
    return render_template('view.html', nodes=nodes, date=now.strftime("%y/%m/%d(%a)"), time=now.strftime("%H:%M:%S"))


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
