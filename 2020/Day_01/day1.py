from itertools import combinations
from math import prod
from aocdays import AoCDay
from timeit import default_timer as timer
from rich.console import Console
from rich.table import Table
from rich import print
day = AoCDay(2020, 1)


# Solution 1 - creating reusable function
def execute(n):
    return next(prod(x) for x in combinations([int(x) for x in open(day.input)], n) if sum(x) == 2020)


day.start = timer()
# Part 1
day.part_one = execute(2)
# Part 2
day.part_two = execute(3)
day.end = timer()
day.print()

# Solution 2 - oneliners
# Part 1
print("Part 1: {}".format([x * y for (x, y) in combinations([int(x) for x in open(day.input)], 2) if x + y == 2020][0]))
print("Part 1: {}".format([prod(x) for x in combinations([int(x) for x in open(day.input)], 2) if sum(x) == 2020][0]))
# Part 2
print("Part 2: {}".format([x * y * z for (x, y, z) in combinations([int(x) for x in open(day.input)], 3) if x + y + z == 2020][0]))
print("Part 2: {}".format([prod(x) for x in combinations([int(x) for x in open(day.input)], 3) if sum(x) == 2020][0]))