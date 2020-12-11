"""Created by Jhesed Tacadena Dec 09, 2020.

Advent of Code Day 9: https://adventofcode.com/2020/day/9

Output:
    Answer: 133015568
"""
from day9.common import PREAMBLE


def find_number(inputs: list) -> int:
    """Finds the first number that doesn't have the following property:

    - not sum of two of the 25 numbers before it
    """

    current_index = 0
    for _ in inputs:

        previous_x_values = inputs[current_index - PREAMBLE : current_index]
        current_value = int(inputs[current_index])
        # print(f"[{current_index}] {current_value}: {previous_x_values:}")
        current_index += 1

        if len(previous_x_values) != PREAMBLE:
            continue
        is_valid = False

        for i in previous_x_values:
            i = int(i)
            for j in previous_x_values:

                j = int(j)
                # print(f"[{current_value}] {i} + {j} = {i + j}")
                if i + j == current_value:
                    is_valid = True
                    break
        if not is_valid:
            print()
            return current_value


if __name__ == "__main__":
    with open("data.txt", "r") as _file:
        _inputs = _file.read().splitlines()
        total_count = find_number(_inputs)
        print(f"Answer: {total_count}")
