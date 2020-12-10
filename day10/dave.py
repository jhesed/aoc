"""Created by Jhesed Tacadena Dec 10, 2020.

Dave's code. Learn by heart. lols
"""
from functools import lru_cache

FILE = "input_revsort.txt"


@lru_cache(maxsize=200)
def find_matches(target: int, tg: int):
    if target == tg:
        return 1
    returnval = 0
    try:
        if lines.index(target - 1):
            returnval += find_matches(target - 1, tg)
    except:
        a = 0
    try:
        if lines.index(target - 2):
            returnval += find_matches(target - 2, tg)
    except:
        a = 0
    try:
        if lines.index(target - 3):
            returnval += find_matches(target - 3, tg)
    except:
        a = 0
    return returnval


lines = []
with open(FILE) as fh:
    for line in fh.readlines():
        adapter = int(line.strip())
        lines.append(adapter)
target = lines[0] + 3
solutions = 0
solutions += find_matches(target - 3, 3)
solutions += find_matches(target - 3, 2)
solutions += find_matches(target - 3, 1)
print(f"There are {solutions} solutions")
