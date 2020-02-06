import numpy as np


class State:
    def __init__(self, puzzle, historic, f=(lambda x, y: 0), indexes_solution=0):
        self.puzzle = puzzle
        self.score = f(puzzle, indexes_solution) + len(historic)
        self.historic = historic

    def __str__(self):
        return np.array_str(self.puzzle)
