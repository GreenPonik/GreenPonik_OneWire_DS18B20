## GreenPonik_OneWire_DS18B20.py Library for Raspberry pi
---------------------------------------------------------
This is the sample code for read temperature with DS18B20 sensor on One Wire bus.

The script auto-detect the 1W file and parse it to find the temperature value.


## Table of Contents

- [## GreenPonik_OneWire_DS18B20.py Library for Raspberry pi](#GreenPonikOneWireDS18B20py-library-for-raspberry-pi)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Methods](#methods)
- [Examples](#examples)
- [Credits](#credits)
<snippet>
<content>

## Installation
```shell
> git clone https://github.com/GreenPonik/GreenPonik_OneWire_DS18B20.git
```
```Python

from GreenPonik_OneWire_DS18B20 import GreenPonik_OneWire_DS18B20

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
from GreenPonik_OneWire_DS18B20 import read_temps

if __name__ == "__main__":
    while True:
        # read both celcius and fahrenheit temperatures
        temperatures = read_temps()
        print("celcius temp %.3f" % temperatures[0])
        print("fahrenheit temp %.3f" % temperatures[1])
        time.sleep(1)
    pass

```

## Credits
Writter by Mickael Lehoux, from [GreenPonik](https://www.greenponik.com), 2019