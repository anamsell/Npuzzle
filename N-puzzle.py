import numpy as np
import sys
import Heuristic
import copy
from End_Puzzle import puzzle_solution_generator
from State import State
import heapq


def adding_close_set(puzzle, close_set, score):
    puzzle = puzzle.flat[:-1]
    for val in puzzle:
        if val not in list(close_set.keys()):
            close_set[val] = dict()
        close_set = close_set[val]
    close_set[0] = score


def is_in_close_set(puzzle, close_set, score):
    value = 1
    puzzle = puzzle.flat[:-1]
    for val in puzzle:
        if val not in list(close_set.keys()):
            return 0
            # close_set[val] = dict()
            # value = 0
        close_set = close_set[val]
    if close_set[0] > score:
        close_set[0] = score
        return 0
    return 1


def puzzle_moves(puzzle_original, size, f, indexes_solution, close_set, open_set):
    x, y = np.where(puzzle_original.puzzle == 0)
    if x != 0:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x - 1, y]
        new_puzzle.puzzle[x - 1, y] = 0
        if not is_in_close_set(new_puzzle.puzzle, close_set, len(new_puzzle.historic) + 1):
            new_puzzle = State(new_puzzle.puzzle, f, indexes_solution, puzzle_original.historic + 'U')
            heapq.heappush(open_set, (new_puzzle.score, new_puzzle.historic, new_puzzle))
    if x != size - 1:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x + 1, y]
        new_puzzle.puzzle[x + 1, y] = 0
        if not is_in_close_set(new_puzzle.puzzle, close_set, len(new_puzzle.historic) + 1):
            new_puzzle = State(new_puzzle.puzzle, f, indexes_solution, puzzle_original.historic + 'D')
            heapq.heappush(open_set, (new_puzzle.score, new_puzzle.historic, new_puzzle))
    if y != size - 1:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x, y + 1]
        new_puzzle.puzzle[x, y + 1] = 0
        if not is_in_close_set(new_puzzle.puzzle, close_set, len(new_puzzle.historic) + 1):
            new_puzzle = State(new_puzzle.puzzle, f, indexes_solution, puzzle_original.historic + 'R')
            heapq.heappush(open_set, (new_puzzle.score, new_puzzle.historic, new_puzzle))
    if y != 0:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x, y - 1]
        new_puzzle.puzzle[x, y - 1] = 0
        if not is_in_close_set(new_puzzle.puzzle, close_set, len(new_puzzle.historic) + 1):
            new_puzzle = State(new_puzzle.puzzle, f, indexes_solution, puzzle_original.historic + 'L')
            heapq.heappush(open_set, (new_puzzle.score, new_puzzle.historic, new_puzzle))


def resolve(puzzle, size, puzzle_solution, function_heuristic, indexes_solution):
    puzzle = State(puzzle, function_heuristic, indexes_solution, '')
    close_set = dict()
    open_set = []
    adding_close_set(puzzle.puzzle, close_set, len(puzzle.historic))
    puzzle_moves(puzzle, size, function_heuristic, indexes_solution, close_set, open_set)
    while open_set:
        if np.array_equal(puzzle.puzzle, puzzle_solution):
            print(puzzle.historic)
            return puzzle
        puzzle = heapq.heappop(open_set)[2]
        adding_close_set(puzzle.puzzle, close_set, len(puzzle.historic))
        puzzle_moves(puzzle, size, function_heuristic, indexes_solution, close_set, open_set)
    print("Problem")


def puzzle_gen(size):
    puzzle_array = np.arange(size*size)
    np.random.shuffle(puzzle_array)
    puzzle_array = puzzle_array.reshape(size, size)
    return puzzle_array


def parser(filename):
    puzzle = []
    size = 0
    max_puzzle = 0
    try:
        with open(filename) as f:
            lines = f.readlines()
        for line in lines:
            line = line[:-1]
            if line == '':
                exit()
            if '#' in line:
                line = line.split("#")[0]
            if line == "":
                continue
            line = line.split(" ")
            line = [empty for empty in line if empty != ""]
            if size == 0:
                if not line[0].isdigit():
                    exit()
                size = int(line[0])
                max_puzzle = size * size - 1
                if size < 3:
                    exit()
                continue
            try:
                puzzle += [[]]
                for value in line:
                    puzzle[-1] += [int(value)]
                    if int(value) > max_puzzle:
                        exit()
            except ValueError:
                exit()
        puzzle_array = np.asarray(puzzle)
        if not (size, size) == puzzle_array.shape:
            exit()
        return puzzle_array, size

    except FileNotFoundError:
        if filename.isnumeric():
            if int(filename) < 3:
                exit()
            return puzzle_gen(int(filename)), int(filename)
        exit()


def main():
    if len(sys.argv) != 2:
        exit()
    puzzle, size = parser(sys.argv[1])
    puzzle_solution, indexes_solution = puzzle_solution_generator(size)
    resolve(puzzle, size, puzzle_solution, Heuristic.linear_conflict_and_manhattan, indexes_solution)


if __name__ == "__main__":
    main()
