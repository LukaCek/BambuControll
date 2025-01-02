import paho.mqtt.client as mqtt
from typing import Dict, Any
import ssl
import time
import json
import logging

class printer:
    def __init__(self, ip: str, printer_id: str, password: str, port: int = 8883, client_id: str = "BambuControll", username: str = "bblp"):
        """Initialize Bambu printer connection."""
        self.printer_ip = ip
        self.printer_id = printer_id
        self.topic = f"device/{printer_id}/report"
        self.port = port
        self.client_id = client_id
        self.username = username
        self.password = password
        self._setup_mqtt_client(self.client_id, self.username, self.password)
        self._initialize_variables()
        self._connect_printer(port)
    
    def _initialize_variables(self):
        """Initialize printer state variables."""
        self.printer_data = {}
        self.bed_temp = None
        self.extruder_temp = None
        self.aux_fan = None
        self.task = None
        self.light = None
    
    def _setup_mqtt_client(self, client_id: str, username: str, password: str):
        """Set up MQTT client with SSL."""
        # Create MQTT client instance
        self.client = mqtt.Client(client_id=client_id, clean_session=True)
        # Set up TLS without certificate validation
        self.client.tls_set(certfile=None, 
                          keyfile=None,
                          cert_reqs=ssl.CERT_NONE,
                          tls_version=ssl.PROTOCOL_TLSv1_2)
        self.client.tls_insecure_set(True)
        # Set username and password
        self.client.username_pw_set(username, password)
        self._setup_callbacks()
    
    def _setup_callbacks(self):
        """Set up MQTT callbacks."""
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                logging.info(f"Connected successfully to {self.printer_ip}")
                client.subscribe(self.topic)
            else:
                logging.error(f"Connection failed with code {rc}")
        
        def on_message(client, userdata, msg):
            try:
                data = json.loads(msg.payload.decode())
                self._update_printer_state(data)
                print(f"### Printer recived: {data}")
            except json.JSONDecodeError:
                logging.error("### Failed to decode printer message")

        self.client.on_connect = on_connect
        self.client.on_message = on_message
    
    def _update_printer_state(self, data: dict[str, Any]):
        """Update internal printer state from MQTT message."""
        for category, values in data.items():
            if category not in self.printer_data:
                self.printer_data[category] = {}
            self.printer_data[category].update(values)
            self.printer_data[category]['last_updated'] = time.time()

        if 'print' in data:
            self.bed_temp = self.printer_data['print'].get('bed_temper')
            self.extruder_temp = self.printer_data['print'].get('nozzle_temper')
            self.aux_fan = self.printer_data['print'].get('big_fan1_speed')
            self.task = self.printer_data['print'].get('mc_print_sub_stage')

        if 'system' in data:
            self.light = self.printer_data['system'].get('led_mode')
    
    def _connect_printer(self, port: int):
        """Establish connection to printer."""
        self.client.connect(self.printer_ip, port, keepalive=60)
        self.client.loop_start()
        time.sleep(2)  # Allow time for connection
    
    ################## Printer functions ##################
    ################## Printer functions ##################

    def set_bed_temp(self, temp):
        self.send_qcode(f"M140 S{temp}")
        self.bed_temperature("<", temp)
    
    def set_extruder_temp(self, temp):
        self.send_qcode(f"M104 S{temp}")
        self.extruder_temperature("<", temp)

    def push(self, filename = "push.gcode", under_temperature = 30):
        self.bed_temperature(">", under_temperature)
        with open(filename, "r") as file:
            for line in file:
                if line.strip() == "done":
                    break
                print(f"Sending: {line.strip()}")
                self.send_qcode(line)
        time.sleep(100)

    def bed_temperature(self, operator = "<", temperature = 35):
        if operator == "<":
            while self.bed_temp < temperature:
                print(f"Bed Temp: {self.bed_temp} < {temperature}")
                time.sleep(5)
        elif operator == ">":
            while self.bed_temp > temperature:
                print(f"Bed Temp: {self.bed_temp} > {temperature}")
                time.sleep(30)
        else:
            print("Invalid operator")
    
    def extruder_temperature(self, operator = "<", temperature = 50):
        if operator == "<":
            while self.extruder_temp < temperature:
                print(f"Hotend Temp: {self.extruder_temp} < {temperature}")
                time.sleep(5)
        elif operator == ">":
            while self.extruder_temp > temperature:
                print(f"Hotend Temp: {self.extruder_temp} > {temperature}")
                time.sleep(30)
        else:
            print("Invalid operator")

    def wait_to_finish(self):
        while self.task == 0:
            time.sleep(.1)
        
        print(self, "Waiting for printer to finish", end="")
        while True:
            if self.task == 0:
                break
            time.sleep(.1)
            print(".", end="")
        print("")

    def light(self, state = "on"):
        command_dict = {
            "system": {
                "sequence_id": "0",
                "command": "ledctrl",
                "led_node": "chamber_light",
                "led_mode": state,
                "led_on_time": 500,
                "led_off_time": 500,
                "loop_times": 0,
                "interval_time": 0
            }
        }
        self.client.publish(self.topic, json.dumps(command_dict))

    def background(self):
        self.light("on")
        self.send_qcode("M17 X0.3 Y0.3")
        self.send_qcode("G1 X230 F400")
        self.send_qcode("G1 Y40")
        self.send_qcode("G1 X40")
        self.send_qcode("G1 Y230")
        self.send_qcode("M17 X1 Y1 Z1")

    def send_qcode(self, command):
        command_dict = {
            "print": {
                "command": "gcode_line",
                "param": command,
                "sequence_id": "0"
            }
        }
        self.client.publish(self.topic, json.dumps(command_dict))
        time.sleep(0.1)
    
    def start_print(self, filename, plate = 1, use_ams=False, timelapse=False, flow_cali=False, bed_leveling=False, layer_inspect=False, vibration_cali=False):
        command_dict = {
            "print": {
            "command": "project_file",
            "url": f"file:///sdcard/{filename}",
            "param": f"Metadata/plate_{plate}.gcode",
            "subtask_id": "0",
            "use_ams": use_ams,
            "timelapse": timelapse,
            "flow_cali": flow_cali,
            "bed_leveling": bed_leveling,
            "layer_inspect": layer_inspect,
            "vibration_cali": vibration_cali
          }
        }
        self.client.publish(self.topic, json.dumps(command_dict))
        time.sleep(0.1)

    def home(self):
        self.send_qcode("G28")