from bambucontroll import printer
import time

# TODO: rendomise personal printer data
printer = printer(
    ip="192.168.1.244",
    printer_id="01P00A000000000",
    password="24661618"
)
printer.light()
printer.set_bed_temperature(35, white=True)
print("TOP")
printer.push()
printer.light("off")