import PyKit
import PuzzleParser
import PuzzleChecker
import A_star
import Uniform_cost_search
import Greedy_search
import Display_solution
import Heuristic
import numpy as np
from Puzzle import Puzzle
from End_Puzzle import puzzle_solution_generator


def heuristic_function(flag_value):
    if flag_value == "hamming":
        return Heuristic.hamming_distance
    elif flag_value == "manhattan":
        return Heuristic.manhattan_distance
    elif flag_value == "linear":
        return Heuristic.linear_conflict_and_manhattan
    else:
        return None


def resolve_algorithm(flag_value, puzzle, puzzle_solution, function, indexes_solution):
    if flag_value == "a*":
        return A_star.resolve(puzzle.puzzle, puzzle.dimension, puzzle_solution, function, indexes_solution)
    elif flag_value == "uniform_cost":
        return Uniform_cost_search.resolve(puzzle.puzzle, puzzle.dimension, puzzle_solution)
    elif flag_value == "greedy_search":
        return Greedy_search.resolve(puzzle.puzzle, puzzle.dimension, puzzle_solution, function, indexes_solution)
    else:
        return None


if __name__ == "__main__":
    PyKit.CommandLine.register_usage("usage: python n-puzzle [file_name]")
    PyKit.CommandLine.register_flag("h",
                                    "The heurisitic function that will be used to solve the puzzle. Can use hamming, manhattan or linear. Default is manhattan.",
                                    default_value="manhattan")
    PyKit.CommandLine.register_flag("a",
                                    "The algorithm that will be used to solve the puzzle. Can use a*, uniform_cost or greedy_search. Default is a*.",
                                    default_value="a*")
    PyKit.CommandLine.show_usage_if_needed()

    file_name = PyKit.CommandLine.get_argument_at_index(1)
    heuristic = PyKit.CommandLine.get_value_for_flag("h")

    if file_name.isdigit():
        if int(file_name) < 3:
            PyKit.Display.error("Puzzle dimension should be greater then 2.")
        dimension = int(file_name)
        while True:
            puzzle_array = PuzzleParser.puzzle_gen(dimension)
            puzzle = Puzzle(puzzle_array, dimension)
            if PuzzleChecker.is_puzzle_solvable(puzzle):
                break
    else:
        puzzle = PuzzleParser.get_puzzle_from_file_name(file_name)

    function = heuristic_function(heuristic)
    if function is None:
        PyKit.Display.error(heuristic + " is not a valid heuristic function. Use hamming, manhattan or linear.")

    if not PuzzleChecker.is_puzzle_solvable(puzzle):
        PyKit.Display.error("This puzzle is not solvable.")

    puzzle_solution, indexes_solution = puzzle_solution_generator(puzzle.dimension)

    algo = PyKit.CommandLine.get_value_for_flag("a")

    # try:
    result = resolve_algorithm(algo, puzzle, puzzle_solution, function, indexes_solution)
    # except:
    #     PyKit.Display.error("This puzzle is not correctly formatted.")

    if (result is None):
        PyKit.Display.error(algo + " is not a valid algorithm. Use a*, uniform_cost or greedy_search")

    result[0].puzzle = puzzle.puzzle
    Display_solution.start(*result)
