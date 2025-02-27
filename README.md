# BambuControll

Python package for controlling Bambu Lab 3D printers (P1 and A1 series) via MQTT

## Installation

```bash
pip install bambucontroll
```

## Basic Usage

```python
from bambucontroll import Printer

# Connect to printer
printer = Printer(
    ip_address="192.168.1.100",
    printer_id="01P00A000000000",
    access_code="12341234")

# Get current status
status = printer.state.printer_data
print(status)

# Start print job
printer.start_print("test.gcode.3mf")
```

## Features
- Real-time printer status monitoring
- Temperature control
- Print job management

## Requirements
- Python 3.8+
- paho-mqtt

## License
MIT