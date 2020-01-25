import sys
import Heuristic
from End_Puzzle import puzzle_solution_generator
import A_star
import numpy as np
import Uniform_cost_search
import Greedy_search
import Display_solution


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
    result = A_star.resolve(puzzle, size, puzzle_solution, Heuristic.linear_conflict_and_manhattan, indexes_solution)
    # result = Uniform_cost_search.resolve(puzzle, size, puzzle_solution)
    # result = Greedy_search.resolve(puzzle, size, puzzle_solution, Heuristic.manhattan_distance, indexes_solution)
    result[0].puzzle = puzzle
    Display_solution.start(*result)


if __name__ == "__main__":
    main()
