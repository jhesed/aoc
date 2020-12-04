"""
    Created by Jhesed Tacadena Dec 03, 2020

    Advent of Code Day 3: https://adventofcode.com/2020/day/3

    Output:
        [0] Trees: 61
        [1] Trees: 257
        [2] Trees: 64
        [3] Trees: 47
        [4] Trees: 37
        Product: 1744787392
"""

TREE = "#"

RULES = [
    # RIGHT, DOWN
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


def count_trees(inputs: list, right: int, down: int) -> int:
    """Counts number of trees (e.g. #) in matrix"""

    trees = 0
    current_right = 0
    current_down = 0

    for _ in inputs:
        try:
            current_down += down
            current_right += right
            next_row = inputs[current_down]
            if next_row[current_right % len(next_row)] == TREE:
                trees += 1

        except IndexError:
            pass  # Reached end of file

    return trees


if __name__ == "__main__":
    product = 1

    # multiply_lines()
    with open("data.txt", "r") as _file:
        _inputs = _file.read().splitlines()

        for counter, rule in enumerate(RULES):
            _right, _down = rule
            trees_count = count_trees(inputs=_inputs, right=_right, down=_down)
            print(f"[{counter}] Trees: {trees_count}")
            product *= trees_count

    print(f"Product: {product}")
