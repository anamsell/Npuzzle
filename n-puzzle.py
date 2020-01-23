import PyKit
import PuzzleParser
import PuzzleChecker


def heuristic_function(flag_value):
    if flag_value == "hamming":
        return "lol"
    elif flag_value == "manhattan":
        return "lol"
    elif flag_value == "linear":
        return "lol"
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
