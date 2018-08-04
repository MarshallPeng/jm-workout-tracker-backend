import json
from src.model.Workout import Workout
from src.constants.FieldNames import UserFieldNames

class User:

    def __init__(self, id, first_name, last_name, email, phone_number, workouts=[]):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.workouts = workouts

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)

    # TODO: Come up with more elegant solution to converting from json to object. Recursive solution maybe?
    @staticmethod
    def fromJSON(json_map):
        user = User(None, None, None, None)
        for key, value in json_map.items():
            if key == 'workouts':
                user.__dict__[key] = []
                for workout in value:
                    user.__dict__[key].append(Workout.fromJSON(workout))
            else:
                user.__dict__[key] = value
        return user


    FIELD_NAMES = {
        UserFieldNames.FIRST_NAME : set_first_name,
        UserFieldNames.LAST_NAME : set_last_name
    }