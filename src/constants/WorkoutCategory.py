from enum import Enum

class WorkoutCategory(Enum):
    CHEST = "Chest"
    BACK = "Back"
    LEGS = "Legs"
    ARMS = "Arms"
    CORE = "Core"


    @staticmethod
    def list():
        return list(map(lambda c: c.value, WorkoutCategory))

