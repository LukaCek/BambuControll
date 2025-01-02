import time
from .mqtt_client import MQTTClient

class printer:
    def __init__(self, ip, port, printer_id, username, password):
        self.mqtt_client = MQTTClient(ip, port, printer_id, username, password)
        self.printer_data = {}
        self.sequence_id = 0

    def set_bed_temp(self, temp):
        self.mqtt_client.send_qcode(f"M140 S{temp}")
        self._wait_for_bed_temperature("<", temp)

    def set_extruder_temp(self, temp):
        self.mqtt_client.send_qcode(f"M104 S{temp}")
        self._wait_for_extruder_temperature("<", temp)

    def push_gcode(self, filename="push.gcode", min_bed_temp=30):
        self._wait_for_bed_temperature(">", min_bed_temp)
        with open(filename, "r") as file:
            for line in file:
                if line.strip() == "done":
                    break
                print(f"Sending: {line.strip()}")
                self.mqtt_client.send_qcode(line)
        time.sleep(.1)  # Adjust sleep as needed

    def _wait_for_bed_temperature(self, operator, temp):
        # Logic to monitor bed temperature
        pass

    def _wait_for_extruder_temperature(self, operator, temp):
        # Logic to monitor extruder temperature
        pass
