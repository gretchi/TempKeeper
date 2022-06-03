#!/usr/bin/env python3

from posixpath import split
from flask import Flask, render_template, request, redirect
from pprint import pprint

from model import Model

app = Flask(__name__)


@app.route('/')
def index():
    model = Model()
    nodes = model.get_nodes()
    model.close()
    return render_template('index.html', nodes=nodes)


@app.route('/set-preset-temp', methods=['POST'])
def set_preset_temp():
    model = Model()
    for k, v in request.form.items():
        prefix, idx = k.split("-")
        if prefix != "preset_temp":
            continue

        model.set_preset_temp(idx, v)

    model.commit()
    model.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8888)
