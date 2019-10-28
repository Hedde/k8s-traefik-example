from flask import Flask, jsonify
app = Flask(__name__)

import socket
hostname = socket.gethostname()

@app.route('/')
def info():
    return jsonify(
        name="service-one",
        host=hostname
    )

@app.route('/topic')
def stock():
    return jsonify(state={
        "apples": 5,
        "oranges": 7
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
