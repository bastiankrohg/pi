from autonomous.obstacles import ObstacleAvoidance
from autonomous.navigation import Navigation
from autonomous.patterns import Patterns
from autonomous.algorithms import Algorithms

class Autonomy:
    def __init__(self):
        self.obstacle_avoidance = ObstacleAvoidance()
        self.navigation = Navigation()
        self.patterns = Patterns()
        self.algorithms = Algorithms()