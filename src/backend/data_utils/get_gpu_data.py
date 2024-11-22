import os
import pandas as pd


def write_gpu_data():
    os.system('nvidia-smi --query-gpu=timestamp,temperature.gpu,utilization.gpu,utilization.memory --format=csv -l 1 > data_utils/data_storage/gpu_data.csv')


def get_gpu_data():
    df = pd.read_csv('data_utils/data_storage/gpu_data.csv')
    cur = df.iloc[-1].to_list()
    
    return cur