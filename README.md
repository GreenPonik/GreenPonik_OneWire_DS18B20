[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_OneWire_DS18B20&metric=alert_status)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_OneWire_DS18B20)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_OneWire_DS18B20&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_OneWire_DS18B20)

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_OneWire_DS18B20&metric=ncloc)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_OneWire_DS18B20)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_OneWire_DS18B20&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_OneWire_DS18B20)

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_OneWire_DS18B20&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_OneWire_DS18B20)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_OneWire_DS18B20&metric=security_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_OneWire_DS18B20)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_OneWire_DS18B20&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_OneWire_DS18B20)


![Upload Python Package](https://github.com/GreenPonik/GreenPonik_OneWire_DS18B20/workflows/Upload%20Python%20Package/badge.svg?event=release)


## GreenPonik_OneWire_DS18B20.py Library for Raspberry pi
---------------------------------------------------------
This is the sample code for read temperature with DS18B20 sensor on One Wire bus.

The script auto-detect the 1W file and parse it to find the temperature value.


## Table of Contents

- [GreenPonik_OneWire_DS18B20.py Library for Raspberry pi](#GreenPonikOneWireDS18B20py-library-for-raspberry-pi)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Methods](#methods)
- [Examples](#examples)
- [Credits](#credits)


## Installation
```shell
> git clone https://github.com/GreenPonik/GreenPonik_OneWire_DS18B20.git
cd GreenPonik_OneWire_DS18B20
pip3 install -r requirements.txt

or 

> pip3 install greenponik-onewire-ds18b20
```
```Python

from GreenPonik_OneWire_DS18B20.GreenPonik_OneWire_DS18B20 import read_temps

```

## Methods

```python
"""
Get temperatues in celcius and fahrenheit
"""
def read_temps():

```

## Example


```Python
import time
from GreenPonik_OneWire_DS18B20.GreenPonik_OneWire_DS18B20 import read_temps

if __name__ == "__main__":
    while True:
        # read both celcius and fahrenheit temperatures
        temperatures = read_temps()
        print("celcius temp %.3f" % temperatures[0])
        print("fahrenheit temp %.3f" % temperatures[1])
        time.sleep(1)

```

## Credits
Write by Mickael Lehoux, from [GreenPonik](https://www.greenponik.com), 2019
