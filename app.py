#!/usr/bin/env python3

from flask import Flask, request, jsonify

import os
import logging

log = logging.getLogger(__name__)
handler = logging.FileHandler("app.log")
formatter = logging.Formatter("%(asctime)s - %(module)s.%(funcName)s: %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)

debug = False
log.setLevel(logging.INFO)
if "FLASK_ENV" in os.environ:
    if os.environ["FLASK_ENV"] == "development":
        debug = True
        log.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    log.debug(request.path)

    if "Accept" in request.headers:
        if "application/json" in request.accept_mimetypes:
            return jsonify({"message": "Good morning"})

    return "<p>Hello, World</p>"

@app.route("/<target>")
def world(target):
    if "lang" in request.args and request.args["lang"] == "es":
        msg = "Hola {}!".format(target)
    else:
        msg = "Hello {}!".format(target)

    if "Accept" in request.headers:
        if "application/json" in request.accept_mimetypes:
            msg = jsonify({"msgs": [msg]})

    return msg

if __name__ == "__main__":
    app.run(debug=debug)
