from data_utils.get_cpu_data import *
from data_utils.get_gpu_data import write_gpu_data, get_gpu_data

from flask import Flask, jsonify
from flask_cors import CORS

import os
import threading

app = Flask(__name__)
CORS(app)

#Initialize cpu class
cpu = CPU()



@app.route('/stats')
def get_stats():

    cpu_data = cpu.output()
    gpu_data = get_gpu_data()
    gpu_temp = int(gpu_data[1])
    gpu_util = int(gpu_data[2][:-2])
    gpu_mem_util = int(gpu_data[3][:-2])

    return jsonify({'cpu_data': cpu_data,'gpu_temp': gpu_temp,'gpu_util':gpu_util,'gpu_mem_util':gpu_mem_util})


if __name__ == '__main__':
    gpu_thread = threading.Thread(target=write_gpu_data, daemon=True)
    gpu_thread.start()
    
    app.run(debug=True)

   
