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

    if len(parsed_lines) == 1 and len(parsed_lines[0]) == 1:
        dimension = int(parsed_lines[0])
        return Puzzle(puzzle_gen(dimension), dimension)
    else:
        n = int(parsed_lines[0])
        puzzle = np.zeros((n, n))

        del parsed_lines[0]

        for (index, line) in enumerate(parsed_lines):
            np_line = np.fromstring(line, dtype=int, sep=" ")
            puzzle[index] = np_line

        return Puzzle(puzzle, n)
