# Solve Sudoku Table

Overview

This is a Python program that solves Sudoku puzzles using a logical approach. It reads a Sudoku grid from an input file, applies solving techniques, and writes the solved grid to an output file while tracking steps.

Features

Reads Sudoku puzzles from a text file

Uses logical rules to find possible numbers for empty cells

Writes each solving step to an output file

Ensures the correct sum of numbers in the Sudoku grid

Requirements

Python 3.x

Usage

Run the script from the command line:

python sudoku_solver.py <input_file> <output_file>

Example

python sudoku_solver.py input.txt output.txt

Input File Format

The input file should contain a 9x9 grid of numbers (0 represents empty cells).

Numbers should be space-separated.

Example input file (input.txt):

5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9

Output File Format

The output file logs the solving steps and the final Sudoku grid.

Example output (output.txt):

------------------
Step 1 - 4 @ R1C3
------------------
5 3 4 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
...
------------------

How It Works

Reads the Sudoku puzzle from the input file.

Iterates through the grid to identify empty cells (0s).

Determines possible numbers for each empty cell using:

Row constraints

Column constraints

3x3 subgrid constraints

If a cell has only one valid possibility, fills it in and records the step.

Repeats the process until the puzzle is solved.

Writes the solution and step-by-step solving process to the output file.
