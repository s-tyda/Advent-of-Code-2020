import operator as op
import numpy as np
import re
import time
from itertools import combinations, product, chain
from functools import reduce, lru_cache
from collections import deque, Counter
from toolz import partition
from math import prod
from array import array
from parse import *
from timeit import default_timer as timer
from aocdays import AoCDay
day = AoCDay(2020, 1)
day.start = timer()

# Your code starts here...


# ...and ends here
day.end = timer()
day.print()