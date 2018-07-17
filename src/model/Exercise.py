

class Exercise:
    MAX_RPE = 10
    MIN_RPE = 0

    def __init__(self, name, weight, total_sets, total_reps, rest_time, rpe):
        self.name = name
        self.weight = weight
        self.rest_time = rest_time
        self.total_sets = total_sets
        self.total_reps = total_reps
        self.completed_sets = 0
        self.completed_reps = 0
        self.completed_volume = 0
        self.expected_volume = total_sets * total_reps * weight
        self.rpe = 0


    def set_rest_time(self, rest_time):
        self.rest_time = rest_time

    def set_weight(self, new_weight):
        self.weight = new_weight

    #When we have a weight incrementer
    def increment_weight(self):
        self.weight += 5

    def complete_rep(self):
        if self.completed_reps < self.total_reps and self.completed_sets < self.total_sets:
            self.completed_reps += 1

            if self.completed_reps >= self.total_reps:
                self.completed_reps = 0
                self.completed_sets += 1

    def is_completed(self):
        return self.completed_sets == self.total_sets

    def get_completed_volume(self):
        return self.completed_sets * self.completed_reps * self.weight

    #Could be potentially used in the future
    def get_expected_volume(self):
        return self.expected_volume

    def set_rpe(self, rpe):
        if rpe > 10 or rpe < 0:
            return -1
        else:
            self.rpe = rpe
            return 0
         








