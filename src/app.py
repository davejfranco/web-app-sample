#!/usr/bin/env python3
from flask import Flask, jsonify
app = Flask(__name__)

VERSION="v0.1"

@app.route('/')
def hello():
    return jsonify(
        {
            "name": "My REST API sample",
            "version": VERSION
        }
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
