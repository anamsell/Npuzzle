# N-Puzzle
Solving a puzzle of any size - School 42 project
## Goals
* Implement A* or one of its variants (Greedy_search/Uniform_cost)
* Implement different heuristic (hamming/manhattan/linear)

Look at subject.pdf for more information

## Requirements:
* `Python 3`
* `NumPy`

## Setup

```
git clone https://github.com/anamsell/Npuzzle.git Npuzzle
cd Npuzzle
pip3 install numpy
```

## Commands

### Examples
```
python3 N_puzzle.py test/solvable/test2 -h Greedy_Search -a uniform_cost
python3 N_puzzle.py test/unsolvable/test4
python3 N_puzzle.py test/invalid/test4
```

### Display Usage
```
python3 N-puzzle
```

## Notes
### Algorithms
* Greedy_Search look for the best move according to the heuristic and make it (very low size complexity, high time complexity, inaccurate result)
* A* store add his next possibles moves to an open list and choose the best move according to the heuristic and the number of move to get this situation (decent size complexity, low time complexity and good result)
* Uniform_Cost operate in a brute-force way. Don't use any heuristic and just try all sequence of moves (that make sense) with the lowest cost until it find a solution (very high size complexity, very high time complexity and best possible result). 

### Heuristics
* Hamming distance is the number of positions at which the corresponding symbols are different.
* Manhattan distance is sum of the number of move along the grid that each tile is displaced from its goal position.
* Linear Conflict is an improvement of manhattan by adding penalty to each pair of conflicting tiles.
