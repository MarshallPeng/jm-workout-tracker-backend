#TODO: Full implementation. just made for tests rn
class User:

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.workouts = []


    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    field_names = {
        "first_name": set_first_name,
        "last_name": set_last_name
    }