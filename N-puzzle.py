import numpy as np
import sys
import Heuristic
import copy
from End_Puzzle import puzzle_solution_generator
from State import State


def get_lowest_score(puzzles):
    best_puzzle = puzzles[0]
    for puzzle in puzzles[1:]:
        if puzzle.score < best_puzzle.score:
            best_puzzle = puzzle
    return best_puzzle


def adding_close_list(puzzle, close_list):
    for i in list(puzzle)[:1]:
        if i not in close_list.keys():
            close_list[i] = dict()
        close_list = close_list[i]


def puzzle_moves(puzzle_original, size, f, indexes_solution, historic):
    puzzles = []
    x, y = np.where(puzzle_original.puzzle == 0)
    if x != 0:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x - 1, y]
        new_puzzle.puzzle[x - 1, y] = 0

        puzzles += [State(new_puzzle.puzzle, f, indexes_solution, historic + 'L')]
    if x != size - 1:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x + 1, y]
        new_puzzle.puzzle[x + 1, y] = 0
        puzzles += [State(new_puzzle.puzzle, f, indexes_solution, historic + 'R')]
    if y != size - 1:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x, y + 1]
        new_puzzle.puzzle[x, y + 1] = 0
        puzzles += [State(new_puzzle.puzzle, f, indexes_solution, historic + 'D')]
    if y != 0:
        new_puzzle = copy.deepcopy(puzzle_original)
        new_puzzle.puzzle[x, y] = new_puzzle.puzzle[x, y - 1]
        new_puzzle.puzzle[x, y - 1] = 0
        puzzles += [State(new_puzzle.puzzle, f, indexes_solution, historic + 'U')]
    return puzzles


def resolve(puzzle, size, puzzle_solution, function_heuristic, indexes_solution):
    historic = ""
    puzzle = State(puzzle, function_heuristic, indexes_solution, historic)
    open_list = puzzle_moves(puzzle, size, function_heuristic, indexes_solution, historic)
    close_list = dict()
    while open_list:
        if np.array_equal(puzzle.puzzle, puzzle_solution):
            return puzzle
        puzzle = get_lowest_score(open_list)
        adding_close_list(puzzle.puzzle, close_list)
        open_list += puzzle_moves(puzzle, size, function_heuristic, indexes_solution, historic)


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
                if not line[0].isnumeric():
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
    resolve(puzzle, size, puzzle_solution, Heuristic.manhattan_distance, indexes_solution)


if __name__ == "__main__":
    main()
