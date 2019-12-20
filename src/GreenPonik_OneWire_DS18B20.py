"""
####################################################################
####################################################################
####################################################################
#################### GreenPonik_OneWire_DS18B20 ####################
############### Read DS18B20 OneWire through Python3 ###############
####################################################################
####################################################################
####################################################################
"""

import os
import time
import re
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


ONE_WIRE_PATH = '/sys/bus/w1/devices/'


def find_1w_sensor():
    files = [name for name in os.listdir(ONE_WIRE_PATH)]
    # if file not create wait 30sec an retry
    if(len(files) == 0):
        print('w1 file not found wait 30sec an retry')
        time.sleep(30)
        # relaunch script
        os.sys.exit(1)
    else:
        for file in files:
            print("one wire file found: %s" % file)
            if(re.search("^28-[0-9a-z]{12}$", file)):
                temp_sensor = '%s%s/w1_slave' % (ONE_WIRE_PATH, file)
                print("temp_sensor:  %s" % temp_sensor)
        return temp_sensor


def temp_raw():
    # temp_raw() -> read one wire lines
    temp_sensor = find_1w_sensor()
    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temps():
    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()

    temp_output = lines[1].find('t=')
    if temp_output != 1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string)/1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        temperatures = temp_c, temp_f
        # return temperature celcius and fahrenheit
        print('temperature: %0.2f °C' % temperatures[0])
        return temperatures[0]


if __name__ == "__main__":
    read_temps()
    pass