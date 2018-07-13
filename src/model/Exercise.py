class Exercise:

    def __init__(self, name, weight, total_sets, total_reps, rest_time):
        self.name = name
        self.weight = weight
        self.rest_time = rest_time
        self.total_sets = total_sets
        self.total_reps = total_reps
        self.completed_sets = 0
        self.completed_reps = 0
        self.completed_volume = 0

    def complete_rep(self):
        if self.completed_reps < self.total_reps and self.completed_sets < self.total_sets:
            self.completed_reps += 1

            if self.completed_reps >= self.total_reps:
                self.completed_reps = 0
                self.completed_sets += 1

    def is_completed(self):
        return self.completed_sets == self.completed_reps

    
