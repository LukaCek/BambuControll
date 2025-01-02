from bambucontroll import printer
import time
'''
# Conect to the printer
printer = printer(
    ip="192.168.1.244", # IP of the printer
    printer_id="01P00A254352762", # Allso known as "Printer"
    password="52348264" # Allso known as "Access Key"
)'''

printer = printer(
    ip="192.168.1.244",
    printer_id="01P00A392200553",
    password="36137093" 
)
printer.set_bed_temp(0)