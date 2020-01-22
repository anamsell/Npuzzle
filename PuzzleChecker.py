import numpy as np
import itertools


def transpose_and_yield_top(arr):
    while len(arr) > 0:
        yield arr[0]
        arr = list(reversed(list(zip(*arr[1:]))))


def is_puzzle_solvable(puzzle):
    flat_puzzle = list(itertools.chain(*transpose_and_yield_top(puzzle.puzzle)))
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
    
    if puzzle.dimension % 2 != 0:
        return inversions % 2 == 0
    else:
        if puzzle.dimension - empty_frame_row % 2 == 0:
            return inversions % 2 != 0
        else:
            return inversions % 2 == 0
