from GreenPonik_OneWire_DS18B20 import GreenPonik_OneWire_DS18B20

if __name__ == "__main__":
    while True:
        GreenPonik_OneWire_DS18B20.read_temps()
        GreenPonik_OneWire_DS18B20.time.sleep(1)
    pass