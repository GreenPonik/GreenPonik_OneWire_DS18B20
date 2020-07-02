import time
from GreenPonik_OneWire_DS18B20 import GreenPonik_OneWire_DS18B20

if __name__ == "__main__":
    while True:
        # read both celcius and fahrenheit temperatures
        temperatures = GreenPonik_OneWire_DS18B20.read_temps()
        print("celcius temp %.3f" % temperatures[0])
        print("fahrenheit temp %.3f" % temperatures[1])
        time.sleep(1)
