from bambucontroll import printer
import time

printer = printer(
    ip="192.168.1.244",
    printer_id="01P00A392200553",
    password="24661618"
)

printer.heat_extruder_temp(90)
printer.coll_extruder_temp(75)
printer.heat_extruder_temp(80)
printer.coll_extruder_temp(40)