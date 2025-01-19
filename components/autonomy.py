from components.autonomous.obstacles import ObstacleAvoidance
from components.autonomous.navigation import Navigation
from components.autonomous.patterns import Patterns
from components.autonomous.algorithms import Algorithms

class Autonomy:
    def __init__(self):
        self.obstacle_avoidance = ObstacleAvoidance()
        self.navigation = Navigation()
        self.patterns = Patterns()
        self.algorithms = Algorithms()