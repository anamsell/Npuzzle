import numpy as np
import copy
from State import State
import heapq
from Close_set import is_in_close_set, adding_close_set


def puzzle_moves(puzzle_original, size, f, indexes_solution, close_set, open_set):
    x, y = np.where(puzzle_original.puzzle == 0)
    if x != 0:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x - 1, y]
        new_puzzle.puzzle[x - 1, y] = 0
        if not is_in_close_set(new_puzzle.puzzle, close_set, len(new_puzzle.historic) + 1):
            new_puzzle = State(new_puzzle.puzzle, puzzle_original.historic + 'U', f, indexes_solution)
            heapq.heappush(open_set, (new_puzzle.score, new_puzzle.historic, new_puzzle))
    if x != size - 1:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x + 1, y]
        new_puzzle.puzzle[x + 1, y] = 0
        if not is_in_close_set(new_puzzle.puzzle, close_set, len(new_puzzle.historic) + 1):
            new_puzzle = State(new_puzzle.puzzle, puzzle_original.historic + 'D', f,  indexes_solution)
            heapq.heappush(open_set, (new_puzzle.score, new_puzzle.historic, new_puzzle))
    if y != size - 1:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x, y + 1]
        new_puzzle.puzzle[x, y + 1] = 0
        if not is_in_close_set(new_puzzle.puzzle, close_set, len(new_puzzle.historic) + 1):
            new_puzzle = State(new_puzzle.puzzle, puzzle_original.historic + 'R', f, indexes_solution)
            heapq.heappush(open_set, (new_puzzle.score, new_puzzle.historic, new_puzzle))
    if y != 0:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x, y - 1]
        new_puzzle.puzzle[x, y - 1] = 0
        if not is_in_close_set(new_puzzle.puzzle, close_set, len(new_puzzle.historic) + 1):
            new_puzzle = State(new_puzzle.puzzle, puzzle_original.historic + 'L', f, indexes_solution)
            heapq.heappush(open_set, (new_puzzle.score, new_puzzle.historic, new_puzzle))


def resolve(puzzle, size, puzzle_solution, function_heuristic, indexes_solution):
    time_complexity = 0
    size_complexity = 0
    puzzle = State(puzzle, '', function_heuristic, indexes_solution)
    if np.array_equal(puzzle.puzzle, puzzle_solution):
        return puzzle, time_complexity, size_complexity
    close_set = dict()
    open_set = []
    adding_close_set(puzzle.puzzle, close_set, len(puzzle.historic))
    puzzle_moves(puzzle, size, function_heuristic, indexes_solution, close_set, open_set)
    while open_set:
        if len(open_set) > size_complexity:
            size_complexity = len(open_set)
        if np.array_equal(puzzle.puzzle, puzzle_solution):
            return puzzle, time_complexity, size_complexity
        time_complexity += 1
        puzzle = heapq.heappop(open_set)[2]
        adding_close_set(puzzle.puzzle, close_set, len(puzzle.historic))
        puzzle_moves(puzzle, size, function_heuristic, indexes_solution, close_set, open_set)
    print("Problem")
