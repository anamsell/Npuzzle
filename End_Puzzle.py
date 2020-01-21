import numpy as np


def puzzle_solution_generator(size):
    puzzle_solution = np.random.rand(size*size)
    indexes_list = []
    x = 0
    y = 0
    ix = 1
    iy = 0
    max_x = size
    max_y = size
    for n in range(1, size * size):
        puzzle_solution[y * size + x] = n
        indexes_list.append((x, y))
        if x + ix == max_x:
            ix = 0
            iy = 1
        if y + iy == max_y:
            ix = -1
            iy = 0
        if x + ix < size-max_x:
            max_y -= 1
            ix = 0
            iy = -1
        if y + iy < size-max_y:
            max_x -= 1
            ix = 1
            iy = 0
        x += ix
        y += iy
    puzzle_solution[y * size + x] = 0
    puzzle_solution = puzzle_solution.reshape(size, size)
    return puzzle_solution, indexes_list
