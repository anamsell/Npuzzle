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

    if not len(parsed_lines):
        PyKit.error("Empty file.")
    else:
        try:
            n = int(parsed_lines[0])
        except ValueError:
            PyKit.error("There is no size at the beginning of the file.")
        if n < 3:
            PyKit.error("Puzzle dimension should be greater then 2.")
        puzzle = np.zeros((n, n))
        del parsed_lines[0]
        if len(parsed_lines) != n:
            PyKit.error("There is " + str(len(parsed_lines)) + " lines , must be "
                        + str(n) + " lines, puzzle is not well formatted.")
        for (index, line) in enumerate(parsed_lines):
            np_line = np.fromstring(line, dtype=int, sep=" ")
            if len(np_line) != n:
                PyKit.error("Line " + str(index + 1) + " is too long or too short, "
                                                       "must be " + str(n) + " values, puzzle is not well formatted.")
            for val in np_line:
                if val > (n * n) - 1 or val < 0:
                    PyKit.error(str(val) + " is greater than " + str(n * n - 1) + " or negative, puzzle is not well "
                                                                                  "formatted.")
                if val in number_founded:
                    PyKit.error(str(val) + " is more then 1 time in the puzzle, puzzle is not well formatted.")
                number_founded += [val]
            puzzle[index] = np_line
        return Puzzle(puzzle, n)
