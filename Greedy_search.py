import numpy as np
import copy
from State import State
from Close_set import is_in_close_set_greedy_uniform, adding_close_set_greedy_uniform
import sys


def go_back(puzzle):
    x, y = np.where(puzzle.puzzle == 0)
    if puzzle.historic[-1] == 'U':
        puzzle.puzzle[x, y] = puzzle.puzzle[x + 1, y]
        puzzle.puzzle[x + 1, y] = 0
    elif puzzle.historic[-1] == 'D':
        puzzle.puzzle[x, y] = puzzle.puzzle[x - 1, y]
        puzzle.puzzle[x - 1, y] = 0
    elif puzzle.historic[-1] == 'R':
        puzzle.puzzle[x, y] = puzzle.puzzle[x, y - 1]
        puzzle.puzzle[x, y - 1] = 0
    else:
        puzzle.puzzle[x, y] = puzzle.puzzle[x, y + 1]
        puzzle.puzzle[x, y + 1] = 0
    puzzle.historic = puzzle.historic[:-1]


def puzzle_moves(puzzle_original, size, f, indexes_solution, close_set):
    score = sys.maxsize
    puzzle = 0
    x, y = np.where(puzzle_original.puzzle == 0)
    if x != 0:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x - 1, y]
        new_puzzle.puzzle[x - 1, y] = 0
        if not is_in_close_set_greedy_uniform(new_puzzle.puzzle, close_set):
            new_puzzle = State(new_puzzle.puzzle, puzzle_original.historic + 'U', f, indexes_solution)
            if score > new_puzzle.score:
                puzzle = new_puzzle
                score = puzzle.score
    if x != size - 1:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x + 1, y]
        new_puzzle.puzzle[x + 1, y] = 0
        if not is_in_close_set_greedy_uniform(new_puzzle.puzzle, close_set):
            new_puzzle = State(new_puzzle.puzzle, puzzle_original.historic + 'D', f,  indexes_solution)
            if score > new_puzzle.score:
                puzzle = new_puzzle
                score = puzzle.score
    if y != size - 1:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x, y + 1]
        new_puzzle.puzzle[x, y + 1] = 0
        if not is_in_close_set_greedy_uniform(new_puzzle.puzzle, close_set):
            new_puzzle = State(new_puzzle.puzzle, puzzle_original.historic + 'R', f, indexes_solution)
            if score > new_puzzle.score:
                puzzle = new_puzzle
                score = puzzle.score
    if y != 0:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x, y - 1]
        new_puzzle.puzzle[x, y - 1] = 0
        if not is_in_close_set_greedy_uniform(new_puzzle.puzzle, close_set):
            new_puzzle = State(new_puzzle.puzzle, puzzle_original.historic + 'L', f, indexes_solution)
            if score > new_puzzle.score:
                puzzle = new_puzzle
                score = puzzle.score
    if score == sys.maxsize:
        go_back(puzzle_original)
        return puzzle_moves(puzzle_original, size, f, indexes_solution, close_set)
    return puzzle


def resolve(puzzle, size, puzzle_solution, function_heuristic, indexes_solution):
    time_complexity = 0
    size_complexity = 0
    puzzle = State(puzzle, '', function_heuristic, indexes_solution)
    close_set = dict()
    adding_close_set_greedy_uniform(puzzle.puzzle, close_set)
    while not np.array_equal(puzzle.puzzle, puzzle_solution):
        time_complexity += 1
        size_complexity = 4
        adding_close_set_greedy_uniform(puzzle.puzzle, close_set)
        puzzle = puzzle_moves(puzzle, size, function_heuristic, indexes_solution, close_set)
    return puzzle, time_complexity, size_complexity
