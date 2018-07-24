class Workout:

    def __init__(self, title, exercises, category, is_repeated, date):
        self.title = title
        self.exercises = exercises
        self.category = category
        self.is_repeated = is_repeated
        self.date = date

    def add_exercise(self, exercise):
        self.exercises.add(exercise)


