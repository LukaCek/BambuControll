from bambucontroll import printer
import time

printer = printer(
    ip="192.168.1.244",
    printer_id="01P00A000000000",
    password="12341234"
)
printer.debug = True

printer.start_print("Rose.gcode.3mf", use_ams=True, timelapse=True)
printer.push(under_temperature=26, object_hight=41.3)