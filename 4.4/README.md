# Recursive Fractal Art — README

## Overview
Fractal generator that draws a recursive snowflakeish pattern and reports the total number of recursive calls. 

## How to run
  - cd /workspaces/class-exercises-Jac0b67/4.4
  - python3 project.py

## Testing
A test helper `run_tests()` replaces the turtle pen with a DummyPen and validates `draw_tree` return values against the closed-form formula for the recurrence:
T(0) = 0  
T(n) = 1 + 3*T(n-1)  =>  T(n) = (3^n - 1) / 2

The test runner exits with code 0 on success and non-zero on failure.

## Debugging & testing process
-Continually tested `draw_tree` with small levels (0, 1, 2) to verify base case and first recursive calls.
-Used print statements to trace recursive calls and ensure correct counting.

## Reasonable recursion depth
- Growth: number of calls grows ~ 3^n. Use `settings["max_levels"]` (default 9) to avoid excessive drawing.
- Recommendations:
  - Small (0–3): quick and useful for debugging
  - Medium (4–6): visible fractal and still responsive
  - Large (7–9): slower and will take minutes
  - Above 9: not recommended 

## Further notes
- Tests are algorithmic and do not validate the graphical output quality. Visual testing requires running the script and observing the turtle window.
- To extend testing, add unit tests for input validation and color parsing, or move core logic into pure functions to further decouple from turtle side effects.


