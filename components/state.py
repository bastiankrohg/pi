class State:
    def __init__(self):
        self.current_state = "IDLE"

    def switch_state(self, new_state):
        # Example states: "IDLE", "RANDOM_WALK", "EXPLORATION", "PURSUIT"
        self.current_state = new_state
