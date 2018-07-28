import json
from src.constants.FieldNames import WorkoutFieldNames
from src.constants import WorkoutCategory

class Workout:

    def __init__(self, id, name, exercises, category, is_repeated, date):
        self.id = id
        self.name = name
        self.exercises = exercises
        self.category = category
        self.is_repeated = is_repeated
        self.date = date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def add_exercise(self, exercise):
        self.exercises.add(exercise)

    def set_name(self, name):
        self.name = name

    def set_category(self, category):
        if category in WorkoutCategory:
            self.category = category

    def set_is_repeated(self, is_repeated):
        if type(is_repeated) == type(True):
            self.is_repeated = is_repeated

    def set_date(self, date): # Will have to use more sophisticated way of representing date
        self.date = date

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)

    @staticmethod
    def fromJSON(json_map):
        workout = Workout(None, None, [], None, None, None)
        for key, value in json_map.items():
            workout.__dict__[key] = value
        return workout


    FIELD_NAMES = {
        WorkoutFieldNames.CATEGORY : set_category,
        WorkoutFieldNames.NAME : set_name,
        WorkoutFieldNames.IS_REPEATED : set_is_repeated,
        WorkoutFieldNames.DATE : set_date
    }