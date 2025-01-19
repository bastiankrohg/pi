from components.state import State
from components.pi_telemetry import Telemetry
from components.autonomy import Autonomy
from components.locomotion import Locomotion
from components.pi_vision import Vision


class Rover:
    def __init__(self):
        self.state = State()
        self.telemetry = Telemetry()
        self.autonomy = Autonomy()
        self.locomotion = Locomotion()
        self.vision = Vision()



