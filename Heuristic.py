

def manhattan_distance(puzzle, puzzle_solution):
    score = 0
    for index1, line in enumerate(puzzle):
        for index2, value in enumerate(line):
            if value == 0:
                continue
            score += abs(index1 - puzzle_solution[value - 1][0]) + abs(index2 - puzzle_solution[value - 1][1])
    return score


def hamming_distance(puzzle, puzzle_solution):
    score = 0
    for index1, line in enumerate(puzzle):
        for index2, value in enumerate(line):
            if value == 0:
                continue
            if (index1, index2) == puzzle_solution[value-1]:
                score += 1
    return score


def get_areas(start, end, size):
    areas = 0
    abscissa = [start[0], end[0]]
    ordered = [start[1], end[1]]
    abscissa.sort()
    ordered.sort()
    for x in range(abscissa[0] + 1, abscissa[1] + 2):
        for y in range(ordered[0] + 1, ordered[1] + 2):
            areas += x + y * size
    return areas


def conflict(areas_list, new_areas):
    number = 0
    for val in areas_list:
        number += not not val & new_areas
    return number


def linear_conflict_and_manhattan(puzzle, puzzle_solution):
    score = 0
    areas = list()
    size = len(puzzle[0])
    for index1, line in enumerate(puzzle):
        for index2, value in enumerate(line):
            if value == 0:
                continue
            val = abs(index1 - puzzle_solution[value - 1][0]) + abs(index2 - puzzle_solution[value - 1][1])
            if val:
                score += val
                new_area = get_areas((index1, index2), puzzle_solution[value-1], size)
                score += conflict(areas, new_area) * 2
                areas += [new_area]
    return score
