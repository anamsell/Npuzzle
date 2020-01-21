

def manhattan_distance(puzzle, puzzle_solution):
    score = 0
    for index1, line in enumerate(puzzle):
        for index2, value in enumerate(line):
            if value == 0:
                continue
            score += abs(index1 - puzzle_solution[value - 1][1]) + abs(index2 - puzzle_solution[value - 1][0])
    return score


def hamming_distance(puzzle, puzzle_solution):
    score = 0
    for index1, line in enumerate(puzzle):
        for index2, value in enumerate(line):
            if value == 0:
                continue
            if (index1, index2) == puzzle_solution[value]:
                score += 1
    return score


def linear_conflict_and_manhattan(puzzle, puzzle_solution):
    score = 0
    for index1, line in enumerate(puzzle):
        for index2, value in enumerate(line):
            if value == 0:
                continue
            score += abs(index1 - puzzle_solution[value][0]) + abs(index2 - puzzle_solution[value][1])
    return score
