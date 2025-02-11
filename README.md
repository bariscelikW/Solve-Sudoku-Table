# Sudoku Solver

## Overview

This is a Python program that solves Sudoku puzzles using a logical approach. It reads a Sudoku grid from an input file, applies solving techniques, and writes the solved grid to an output file while tracking steps.

## Features

- Reads Sudoku puzzles from a text file

- Uses logical rules to find possible numbers for empty cells

- Writes each solving step to an output file

- Ensures the correct sum of numbers in the Sudoku grid

## Requirements

- Python 3

## Usage

Run the script from the command line:
```
python sudoku.py <input_file> <output_file>
```
## Input File Format

- The input file should contain a 9x9 grid of numbers (0 represents empty cells).

- Numbers should be space-separated.

### Example input file (input.txt):
```
0 4 0 0 0 0 1 7 9
0 0 2 0 0 8 0 5 4
0 0 6 0 0 5 0 0 8
0 8 0 0 7 0 9 1 0
0 5 0 0 9 0 0 3 0
0 1 9 0 6 0 0 4 0
3 0 0 4 0 0 7 0 0
5 7 0 1 0 0 2 0 0
9 2 8 0 0 0 0 6 0
```
## Output File Format

The output file logs the solving steps and the final Sudoku grid.

### Example output (output.txt):
```
------------------
Step 1 - 8 @ R1C1
------------------
8 4 0 0 0 0 1 7 9
0 0 2 0 0 8 0 5 4
0 0 6 0 0 5 0 0 8
0 8 0 0 7 0 9 1 0
0 5 0 0 9 0 0 3 0
0 1 9 0 6 0 0 4 0
3 0 0 4 0 0 7 0 0
5 7 0 1 0 0 2 0 0
9 2 8 0 0 0 0 6 0
------------------
. 
.
.
Step 48 - 1 @ R9C9
------------------
8 4 5 6 3 2 1 7 9
7 3 2 9 1 8 6 5 4
1 9 6 7 4 5 3 2 8
6 8 3 5 7 4 9 1 2
4 5 7 2 9 1 8 3 6
2 1 9 8 6 3 5 4 7
3 6 1 4 2 9 7 8 5
5 7 4 1 8 6 2 9 3
9 2 8 3 5 7 4 6 1
------------------
```
## How It Works

1. Reads the Sudoku puzzle from the input file.

2. Iterates through the grid to identify empty cells (0s).

3. Determines possible numbers for each empty cell using:

   - Row constraints

   - Column constraints

   - 3x3 subgrid constraints

   - If a cell has only one valid possibility, fills it in and records the step.

4. Repeats the process until the puzzle is solved.

5. Writes the solution and step-by-step solving process to the output file.

## License

This project is open-source and available under the MIT License.

bariscelikw

