import PyKit
import PuzzleParser
import PuzzleChecker

if __name__ == "__main__":
    PyKit.CommandLine.register_usage("usage: python n-puzzle [file_name]")
    PyKit.CommandLine.show_usage_if_needed()

    file_name = PyKit.CommandLine.get_argument_at_index(1)
    puzzle = PuzzleParser.get_puzzle_from_file_name(file_name)
    
    print(PuzzleChecker.is_puzzle_solvable(puzzle))
