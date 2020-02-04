import PyKit
import numpy as np
from Puzzle import Puzzle


def puzzle_gen(size):
    puzzle_array = np.arange(size * size)
    np.random.shuffle(puzzle_array)
    puzzle_array = puzzle_array.reshape(size, size)
    return puzzle_array


def get_puzzle_from_file_name(file_name):
    file_content = PyKit.FileManager.get_string_from_file(file_name)
    parser = PyKit.Parser(clear_empty_lines=True, clear_comment_lines=True)
    parsed_lines = parser.parsed_str(file_content)
    number_founded = list()

    if len(parsed_lines) == 1 and len(parsed_lines[0]) <= 2:
        dimension = int(parsed_lines[0])
        return Puzzle(puzzle_gen(dimension), dimension)
    else:
        n = int(parsed_lines[0])
        puzzle = np.zeros((n, n))
        del parsed_lines[0]
        for (index, line) in enumerate(parsed_lines):
            np_line = np.fromstring(line, dtype=int, sep=" ")
            if len(np_line) != n:
                PyKit.error("Line " + str(index + 1) + " is too long or too short, "
                                                   "must be " + str(n) + " values, puzzle is not well formatted.")
            for val in np_line:
                if val > (n * n) - 1:
                    PyKit.error(str(val) + " is greater than " + str(n * n - 1) + " or negative, puzzle is not well "
                                                                                  "formatted.")
                if val in number_founded:
                    PyKit.error(str(val) + " is more then 1 time in the puzzle, puzzle is not well formatted.")
                number_founded += [val]
            puzzle[index] = np_line
        if index != n - 1:
            PyKit.error("There is " + str(index + 1) + " lines , must be " + str(n) + " lines, "
                                                                                      "puzzle is not well formatted.")
        return Puzzle(puzzle, n)
