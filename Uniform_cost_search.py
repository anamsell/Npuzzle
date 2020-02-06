import numpy as np
import copy
from State import State
from Close_set import is_in_close_set_greedy_uniform, adding_close_set_greedy_uniform


def puzzle_moves(puzzle_original, size, close_set):
    open_set = []
    x, y = np.where(puzzle_original.puzzle == 0)
    if x != 0:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x - 1, y]
        new_puzzle.puzzle[x - 1, y] = 0
        if not is_in_close_set_greedy_uniform(new_puzzle.puzzle, close_set):
            new_puzzle = State(new_puzzle.puzzle, puzzle_original.historic + 'U')
            open_set += [new_puzzle]
    if x != size - 1:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x + 1, y]
        new_puzzle.puzzle[x + 1, y] = 0
        if not is_in_close_set_greedy_uniform(new_puzzle.puzzle, close_set):
            new_puzzle = State(new_puzzle.puzzle, puzzle_original.historic + 'D')
            open_set += [new_puzzle]
    if y != size - 1:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x, y + 1]
        new_puzzle.puzzle[x, y + 1] = 0
        if not is_in_close_set_greedy_uniform(new_puzzle.puzzle, close_set):
            new_puzzle = State(new_puzzle.puzzle, puzzle_original.historic + 'R')
            open_set += [new_puzzle]
    if y != 0:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x, y - 1]
        new_puzzle.puzzle[x, y - 1] = 0
        if not is_in_close_set_greedy_uniform(new_puzzle.puzzle, close_set):
            new_puzzle = State(new_puzzle.puzzle, puzzle_original.historic + 'L')
            open_set += [new_puzzle]
    return open_set


def resolve(puzzle, size, puzzle_solution):
    time_complexity = 0
    size_complexity = 0
    puzzles = [State(puzzle, '')]
    if np.array_equal(puzzles[0].puzzle, puzzle_solution):
        return puzzles[0], time_complexity, size_complexity
    close_set = dict()
    open_set = []
    adding_close_set_greedy_uniform(puzzles[0].puzzle, close_set)
    puzzles = puzzle_moves(puzzles[0], size, close_set)
    while puzzles:
        if size_complexity < len(puzzles):
            size_complexity = len(puzzles)
        for val in puzzles:
            time_complexity += 1
            if np.array_equal(val.puzzle, puzzle_solution):
                return puzzles[0], time_complexity, size_complexity
            adding_close_set_greedy_uniform(val.puzzle, close_set)
            open_set += puzzle_moves(val, size, close_set)
        puzzles = open_set
        open_set = []
    print("Problem")
