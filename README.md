# Simplex Method Implementation

This repository contains a Python implementation of the Simplex method for solving linear programming problems. The code is organized into three main files: `my_main_simplex.py`, `main_transformations.py`, and `simplex_algo_functions.py`. 

## Overview

### `my_main_simplex.py`

This file is the entry point for defining and solving the linear programming problem. It contains the following key functions:

- `main`: Defines the linear programming problem, checks for negative values in the constraints, processes the problem using functions from `main_transformations` and then applies the Simplex algorithm from `simplex_algo_functions`.

### `main_transformations.py`

This file contains functions that handle transformations of the problem. These functions include:

- `process_restrictions`: Extracts the P and R arrays from restrictions and calculates the number of extra variables to add.
- `typicalForm`: Converts the linear programming problem into typical form.
- `arrayPrinter`: Prints arrays for debugging purposes.

### `simplex_algo_functions.py`

This file contains the core Simplex algorithm functions, including:

- `found_negative`: Checks if there are negative values in an array.
- `pivot_fun`: Identifies the pivot element for the Simplex method.
- Row operations functions (`rowDivider`, `multiSubRow`, `multiSumRow`, `otherPivot`) to manipulate the tableau.
- The main `simplex_algo` function, which applies the Simplex algorithm to solve the linear programming problem.

## Note

This implementation is a basic example of the Simplex method and can be further extended and optimized for more complex problems and real-world applications.

Please feel free to use, modify, and contribute to this repository as needed.