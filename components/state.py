class State:
    def __init__(self):
        self.current_state = "IDLE"

    def get_state(self):
        return self.current_state

    def set_state(self, new_state):
        if new_state in ["IDLE", "RANDOM_WALK", "EXPLORATION", "PURSUIT"]:
            print(f"Switching from {self.current_state} to {new_state}")
            self.current_state = new_state
        else:
            raise ValueError(f"Invalid state: {new_state}")
