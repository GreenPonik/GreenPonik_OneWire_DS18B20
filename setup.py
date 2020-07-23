from setuptools import setup, find_packages
import os
import pathlib
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "src"))

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')


def load_version():
    version_file = os.path.join(os.path.dirname(
        __file__), "src/GreenPonik_OneWire_DS18B20", "version.py")
    version = {}
    with open(version_file) as fd:
        exec(fd.read(), version)
    return version["__version__"]


setup(
    name="greenponik-onewire-ds18b20",
    version=load_version(),
    author="GreenPonik SAS",
    author_email="contact@greenponik.com",
    description="GreenPonik DS198B20 One Wire read temperature",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GreenPonik/GreenPonik_OneWire_DS18B20",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(where='src'),  # Required
    package_dir={"": "src"},
    python_requires=">=3.6",
    project_urls={  # Optional
        'Source': 'https://github.com/GreenPonik/GreenPonik_OneWire_DS18B20/',
        'Bug Reports': 'https://github.com/GreenPonik/GreenPonik_OneWire_DS18B20/issues',
    },
    keywords="GreenPonik hydroponics DS18B20 OneWire 1Wire temperature reader python hardware diy iot raspberry pi",
    py_modules=["GreenPonik_OneWire_DS18B20"],
)
