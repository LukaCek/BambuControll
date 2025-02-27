from bambucontroll import printer
import time

printer = printer(
    ip="192.168.1.244",
    printer_id="01P00A000000000",
    password="24661618"
)
#printer.debug = True
#printer.home()

while True:
    i = int(input("colling fan speed: "))
    printer.cooling_fan(i)
    i = int(input("chamber fan speed: "))
    printer.chamber_fan(i)
    i = int(input("aux fan speed: "))
    printer.aux_fan(i)
