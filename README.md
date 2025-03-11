# BambuControll

[Full documentation](https://lukacek.github.io/BambuControll/). Also available on [PyPI](https://pypi.org/project/bambucontroll/).

Python package for controlling Bambu Lab 3D printers (P1 and A1 series) via MQTT

## Installation
Library is available on [PyPI](https://pypi.org/project/bambucontroll/) so you can install it with:

```bash
pip install bambucontroll
```

## Basic Usage

```python
from bambucontroll import Printer

# Connect to printer
printer = Printer(
    ip="192.168.1.100",
    printer_id="01P00A000000000",
    password="12341234"
    )

# Get current status
status = printer.state.printer_data
print(status)

# Start print job
printer.start_print("test.gcode.3mf")
```
For more information, see the [full documentation](https://lukacek.github.io/BambuControll/).

## Features
- Real-time printer status monitoring
- Temperature control
- Print job management

## Requirements
- Python 3.8+
- paho-mqtt

## License
MIT
