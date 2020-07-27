from time import sleep
from GreenPonik_OneWire_DS18B20 import read_temps


if __name__ == "__main__":
    try:
        while True:
            # read both celcius and fahrenheit temperatures
            temperatures = read_temps()
            print("celcius temp %.3f" % temperatures[0])
            print("fahrenheit temp %.3f" % temperatures[1])
            sleep(1)
    except Exception as e:
        print("Exception occured", e)
