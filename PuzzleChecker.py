import numpy as np


def is_puzzle_solvable(puzzle):
    flat_puzzle = puzzle.puzzle.flatten()
    empty_frame_row = 0
    inversions = 0

    for i in range(0, puzzle.dimension * puzzle.dimension - 1):
        if flat_puzzle[i] == 0:
            empty_frame_row = int(i / puzzle.dimension)
            continue
        
        for j in range(i + 1, puzzle.dimension * puzzle.dimension):
            first_frame = flat_puzzle[i]
            second_frame = flat_puzzle[j]

            if second_frame == 0:
                continue

            if first_frame > second_frame:
                inversions += 1
    
    if puzzle.dimension % 2 == 0:
        return inversions % 2 == 0
    else:
        if puzzle.dimension - empty_frame_row % 2 == 0:
            return inversions % 2 != 0
        else:
            return inversions % 2 == 0
