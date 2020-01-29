import PyKit
import PuzzleParser
import PuzzleChecker
import A_star
import Uniform_cost_search
import Greedy_search
import Display_solution
import Heuristic
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


if __name__ == "__main__":
    PyKit.CommandLine.register_usage("usage: python n-puzzle [file_name]")
    PyKit.CommandLine.register_flag("h", "The heurisitic function that will be used to solve the puzzle. Can use hamming, manhattan or linear. Default is hamming.", default_value="hamming")
    PyKit.CommandLine.show_usage_if_needed()

    file_name = PyKit.CommandLine.get_argument_at_index(1)
    heuristic = PyKit.CommandLine.get_value_for_flag("h")
    puzzle = PuzzleParser.get_puzzle_from_file_name(file_name)
    
    function = heuristic_function(heuristic)
    if function is None:
        PyKit.Display.error(heuristic + " is not a valid heuristic function. Use hamming, manhattan or linear.")
    
    if not PuzzleChecker.is_puzzle_solvable(puzzle):
        PyKit.Display.error("This puzzle is not solvable.")

    puzzle_solution, indexes_solution = puzzle_solution_generator(puzzle.dimension)
    result = A_star.resolve(puzzle.puzzle, puzzle.dimension, puzzle_solution, function,
                            indexes_solution)
    # result = Uniform_cost_search.resolve(puzzle.puzzle, puzzle.dimension, puzzle_solution)
    # result = Greedy_search.resolve(puzzle.puzzle, puzzle.dimension, puzzle_solution, function, indexes_solution)
    result[0].puzzle = puzzle.puzzle
    Display_solution.start(*result)
