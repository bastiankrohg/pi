from components.state import State
from components.pi_telemetry import Telemetry
from components.autonomy import Autonomy
from components.locomotion import Locomotion
from components.pi_vision import Vision

import threading
import time

class Rover:
    def __init__(self):
        self.autonomy = Autonomy()
        self.locomotion = Locomotion()
        self.vision = Vision()
        self.telemetry = Telemetry(udp_ip='192.168.1.2', udp_port=5005, interval=5)

    def start(self):
        telemetry_thread = threading.Thread(target=self.telemetry.send_data)
        telemetry_thread.daemon = True
        telemetry_thread.start()
        # Start other components...

if __name__ == "__main__":
    rover = Rover()
    rover.start()
    # Keep the main thread running
    while True:
        time.sleep(1)




