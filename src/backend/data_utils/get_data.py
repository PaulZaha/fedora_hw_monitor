import os
import logging
import time
import argparse
import pandas as pd # type: ignore
import numpy as np
import psutil


class CPU:
    def __init__(self):
        self.cpu_count = psutil.cpu_count(logical=False)
        self.logical_cores = psutil.cpu_count(logical=True)
        self.cpu_percent = None
        self.cpu_freq = None
        self.cpu_temp = None
        self.update_stats()
    def update_stats(self):

        self.cpu_percent = psutil.cpu_percent(interval=1)
        freq = psutil.cpu_freq()
        self.cpu_freq = freq.current
        if hasattr(psutil, 'sensors_temperatures'):
            self.cpu_temp = self.get_cpu_temperature()

    def get_cpu_temperature(self):

        try:
            temperatures = psutil.sensors_temperatures()
            if "coretemp" in temperatures:
                core_temps = temperatures["coretemp"]

                return core_temps[0].current if core_temps else None
        except Exception as e:
            pass
        return None

    def output(self):
        try:
            self.update_stats()
            data = {
                'usage': self.cpu_percent,
                'freq': self.cpu_freq,
            }
            if self.cpu_temp is not None:
                data['temp'] = self.cpu_temp

            return data
        except Exception as e:
            return {'success': False}

def main():
    pass
        


if __name__ == '__main__':
    main()