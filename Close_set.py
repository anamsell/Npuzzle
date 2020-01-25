

def adding_close_set(puzzle, close_set, score):
    puzzle = puzzle.flat[:-1]
    for val in puzzle:
        if val not in list(close_set.keys()):
            close_set[val] = dict()
        close_set = close_set[val]
    close_set[0] = score


def is_in_close_set(puzzle, close_set, score):
    puzzle = puzzle.flat[:-1]
    for val in puzzle:
        if val not in list(close_set.keys()):
            return 0
        close_set = close_set[val]
    if close_set[0] > score:
        close_set[0] = score
        return 0
    return 1


def adding_close_set_greedy_uniform(puzzle, close_set):
    puzzle = puzzle.flat[:-1]
    for val in puzzle:
        if val not in list(close_set.keys()):
            close_set[val] = dict()
        close_set = close_set[val]


def is_in_close_set_greedy_uniform(puzzle, close_set):
    puzzle = puzzle.flat[:-1]
    for val in puzzle:
        if val not in list(close_set.keys()):
            return 0
        close_set = close_set[val]
    return 1
