# Fractal project (4.4)

This folder contains `project.py`, a recursive fractal program.

What is included
- `project.py` — drawing program that uses recursion.
- `fractal_core.py` — module that computes expected recursive-call counts.

How to run this program:

Follow the prompt for recursion levels. Reasonable levels are 0-6. Very high
levels may take a long time to draw or cause the program to be slow.

Expected output (example):

```
level=0: expected=0, got=0
level=1: expected=1, got=1
level=2: expected=4, got=4
level=3: expected=13, got=13
All tests passed.
```

What the tests verify
- The `project.py` implementation counts recursive calls using the recurrence
  T(0)=0, T(n)=1 + 3*T(n-1). `fractal_core.expected_calls` computes the same
  values without needing the turtle graphics, so it can be used in automated
  tests.

Notes on recursion depth and performance
- The drawing function issues 3 recursive calls per non-base node. That means
  the number of calls grows exponentially with depth. The growth factor per level
  is approximately the number of branches which is 3.
- Recommended levels: Around 0–6. Values higher than 7 take much longer to run.

Testing and debugging
- I ran `project.py` with a small level(1-3) and observed
  the pattern.


