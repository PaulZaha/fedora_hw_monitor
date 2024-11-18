import os
import logging
import time
import argparse
import pandas as pd # type: ignore

parser = argparse.ArgumentParser(prog='Fedora_Hardware_Monitor')
parser.add_argument('-i', '--interval', default=1)
args = parser.parse_args()


interval = float(args.interval)



def get_cpu_temps():
    """
    Returns list of all CPU temp sensors 
    """
    try:
        dir = os.path.join('/','sys','class','thermal')

    except FileNotFoundError:
        return None
    
    temp_list = []
    gen = (file for file in os.listdir(dir) if 'thermal_zone' in file)

    for file in gen:
        temp = open(os.path.join(dir,file,'temp'),'r')
        temp_list.append(int(temp.read())/1000)

    print(temp_list)
    return temp_list

def loop_cpu_temps():
    
    while True:
        get_cpu_temps()
        time.sleep(interval)

def get_cpu_usage():
    """_summary_

    Returns:
        _type_: _description_
    """
    try:
        dir = os.path.join('/','proc')

    except FileNotFoundError:
        return None
    
    file = open(os.path.join(dir,'stat'),'r')
    print(file.read())
    

def main():
    #loop_cpu_temps()
    get_cpu_usage()

        


if __name__ == '__main__':
    main()