# python Sudoku Solver
### you can use this class to solve an n*n sudoku

it's very simple to use
for example i have an 3*3 sudoku:
```python
from solver import Solver
table = [
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, 0]
]
solver_object = Solver(table)
# solve method return an stack that contains the answer
# each level of answer pushed to this stack
stack_answer = solver_object.solve()
# if sudoku is unsolvable, the stack is empty
for level in stack_answer:
    for line_of_level_list in level:
        print(line_of_level_list)
    print()
    print()

"""
output:
[2, 1, 0]
[1, 0, 0]
[0, 0, 0]


[2, 1, 3]
[1, 0, 0]
[0, 0, 0]


[2, 1, 3]
[1, 0, 2]
[0, 0, 0]


[2, 1, 3]
[1, 3, 2]
[0, 0, 0]


[2, 1, 3]
[1, 3, 2]
[3, 0, 0]


[2, 1, 3]
[1, 3, 2]
[3, 2, 0]


[2, 1, 3]
[1, 3, 2]
[3, 2, 1]
"""

```
## in addition
### for 9*9 sudokus, we considered the sections
