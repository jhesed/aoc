"""
    Created by Jhesed Tacadena Dec 03, 2020

    Advent of Code Day 3: https://adventofcode.com/2020/day/3
"""

COUNT = 300
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
            if next_row[current_right] == TREE:
                trees += 1

        except IndexError:
            pass  # Reached end of file

    return trees


def multiply_lines():
    """
    Multiply lines to produce larger image.
    TODO: This is very messy. Don't do this at home
    """
    content = ""

    with open("data/day3.txt", "r") as _file:
        _inputs = _file.read().splitlines()
        for line in _inputs:
            content += f"{line * COUNT}\n"

    with open("data/day3_edited.txt", "w") as _file:
        _file.write(content)


if __name__ == "__main__":
    product = 1

    multiply_lines()
    with open("data/day3_edited.txt", "r") as _file:
        _inputs = _file.read().splitlines()

        for rule in RULES:
            right, down = rule
            product *= count_trees(inputs=_inputs, right=right, down=down)

    print(f"Final Answer: {product}")
