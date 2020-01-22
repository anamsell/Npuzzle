import PyKit
import numpy as np

def get_puzzle_from_file_name(file_name):
    file_content = PyKit.FileManager.get_string_from_file(file_name)
    parser = PyKit.Parser(clear_empty_lines=True, clear_comment_lines=True)
    parsed_lines = parser.parsed_str(file_content)
    n = int(parsed_lines[0])
    puzzle = np.zeros((n, n))

    del parsed_lines[0]
    
    for (index, line) in enumerate(parsed_lines):
        np_line = np.fromstring(line, dtype=int, sep=" ")
        puzzle[index] = np_line

    return puzzle
