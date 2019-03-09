from collections import defaultdict
from itertools import product
from random import randint
from timeit import default_timer

import functions as func


functions = [getattr(func, name) for name in dir(func) if not name.startswith("__")]

n_needles = [2, 5, 10, 25]
haystacks_maxiter = [(10, 1000), (100, 1000), (1000, 1000), (100_000, 10)]
n_values = [4, 8, 32, 128]

iterations = 1000

for f in functions:
    f.results = defaultdict(lambda: 0)

for n, h_i, v in product(n_needles, haystacks_maxiter, n_values):
    h, iterations = h_i
    for _ in range(iterations):
        needles = [randint(1, v) for _ in range(n)]
        haystack = [randint(1, v) for _ in range(h)]

        for f in functions:
            start = default_timer()
            f(haystack, needles)
            f.results[(n, h, v)] += default_timer() - start

for f in functions:
    print(f.__name__)
    print(f.results)
