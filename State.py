import numpy as np

class State:
    def __init__(self, puzzle, f, indexes_solution, historic):
        self.puzzle = puzzle
        self.score = f(puzzle, indexes_solution) + len(historic)
        self.historic = historic

    def __str__(self):
        return np.array_str(self.puzzle)
