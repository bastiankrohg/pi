# components/telemetry.py
import psutil
import socket
import json
import time
import os

class Telemetry:
    def __init__(self, udp_ip='192.168.1.2', udp_port=5005, interval=5):
        self.udp_ip = udp_ip
        self.udp_port = udp_port
        self.interval = interval
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def get_cpu_temperature(self):
        # For Raspberry Pi, read the CPU temperature
        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
                temp = f.readline()
            return float(temp) / 1000.0
        except FileNotFoundError:
            return None

    def get_system_metrics(self):
        metrics = {
            'cpu_temperature': self.get_cpu_temperature(),
            'cpu_usage': psutil.cpu_percent(interval=1),
            'memory_usage': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent,
            'timestamp': time.time()
        }
        return metrics

    def send_data(self):
        while True:
            metrics = self.get_system_metrics()
            message = json.dumps(metrics)
            self.sock.sendto(message.encode(), (self.udp_ip, self.udp_port))
            time.sleep(self.interval)