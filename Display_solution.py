import numpy as np


def puzzle_representation(puzzle):
    string = ""
    for val in puzzle:
        for val2 in val:
            string += str(val2) + ' '
        string = string[:-1] + '\n'
    return string + '\n'


def move_puzzle(puzzle, move):
    x, y = np.where(puzzle == 0)
    if move == 'D':
        puzzle[x, y] = puzzle[x + 1, y]
        puzzle[x + 1, y] = 0
    elif move == 'U':
        puzzle[x, y] = puzzle[x - 1, y]
        puzzle[x - 1, y] = 0
    elif move == 'L':
        puzzle[x, y] = puzzle[x, y - 1]
        puzzle[x, y - 1] = 0
    else:
        puzzle[x, y] = puzzle[x, y + 1]
        puzzle[x, y + 1] = 0


def path_to_solution(puzzle, historic):
    result_print = puzzle_representation(puzzle)
    while historic:
        move_puzzle(puzzle, historic[0])
        result_print += puzzle_representation(puzzle)
        historic = historic[1:]
    print(result_print)


def start(puzzle, time_complexity, size_complexity):
    path_to_solution(puzzle.puzzle, puzzle.historic)
    print("Time complexity is " + str(time_complexity))
    print("Size complexity is " + str(size_complexity))
    print("The number of moves is " + str(len(puzzle.historic)))
    exit()
