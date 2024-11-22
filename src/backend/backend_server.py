from data_utils.get_data import *

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#Initialize cpu class
cpu = CPU()


@app.route('/stats')
def get_stats():

    data = cpu.output()
    print(data)

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
